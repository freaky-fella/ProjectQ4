import pygame
from settings import GROUND_Y, JUMP_STRENGTH, GRAVITY, CYAN, SCREEN_HEIGHT, SCREEN_WIDTH, BLACK, WHITE, FPS
from player import Player
from levelManager import LevelManager
from gameUI import GameUI

class GameManager:
    def __init__(self):

        

        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Geometry Dash Clone")
        self.clock = pygame.time.Clock()
        self.state = "MENU"
        
        self.player = Player()
        self.level_manager = LevelManager()
        self.ui = GameUI()
    
        self.bg_image = pygame.image.load("backgroundimage.png").convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bg_x = 0
        self.bg_speed = 2
    
    def check_collisions(self):
        # self.player.on_ground = (self.player.rect.bottom >= GROUND_Y)

        for obs in self.level_manager.obstacles:
            if self.player.death_rect.colliderect(obs.rect):
                self.state = "GAMEOVER"

        for plat in self.level_manager.platforms:
            if self.player.rect.colliderect(plat.rect):
                if self.player.vel_y >= 0 and self.player.rect.bottom < plat.rect.top + 20:
                    self.player.rect.bottom = plat.rect.top
                    self.player.vel_y = 0
                    self.player.on_ground = True

                    continue
                if self.player.death_rect.colliderect(plat.rect):
                    self.state = "GAMEOVER"
        for p in self.level_manager.portals:
            if self.player.rect.colliderect(p.rect) and not p.activated:
                self.player.mode = p.target_mode
                p.activated = True 
                
                if self.player.mode == "WAVE":
                    self.player.vel_y = 0 
                    self.player.trail_points = []
                else:
                    self.player.on_ground = False

    def run(self):
        running = True
        while running:
            

            self.screen.fill(BLACK) 

            if self.bg_image:
                self.screen.blit(self.bg_image, (self.bg_x, 0))
                self.screen.blit(self.bg_image, (self.bg_x + SCREEN_WIDTH, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    # Toggle hitboxes with 'H'
                    if event.key == pygame.K_h:
                        self.level_manager.show_hitboxes = not self.level_manager.show_hitboxes
                    
                    # Jump / Restart logic
                    if event.key == pygame.K_SPACE:
                        if self.state == "PLAYING":
                            # The jump is actually handled in player.handle_input, 
                            # but some people put it here.
                            pass 
                        elif self.state in ["MENU", "GAMEOVER", "VICTORY"]:
                            self.level_manager.reset()
                            self.state = "PLAYING"

            if self.state == "PLAYING":
                self.player.handle_input()
                
                if self.player.mode == "WAVE":
                    self.player.apply_wave_physics()
                else:
                    self.player.apply_gravity()
                    
                self.level_manager.update()
                self.check_collisions()
                # 1. Update the position
                self.bg_x -= self.bg_speed 
                
                # 2. The Reset Logic
                # If the image has slid one full screen width to the left, snap it back
                if self.bg_x <= -SCREEN_WIDTH:
                    self.bg_x = 0
                self.level_manager.update()
                self.check_collisions()
                
                if self.level_manager.check_win():
                    self.state = "VICTORY"


            pygame.draw.line(self.screen, WHITE, (0, GROUND_Y), (SCREEN_WIDTH, GROUND_Y), 2)
            
            if self.state == "PLAYING" or self.state == "GAMEOVER" or self.state == "VICTORY":
                self.player.draw(self.screen)
                
                for obs in self.level_manager.obstacles:
                    obs.draw(self.screen)
                for plat in self.level_manager.platforms:
                    plat.draw(self.screen)
                for p in self.level_manager.portals:
                    p.draw(self.screen)
                if self.level_manager.show_hitboxes:
                    pygame.draw.rect(self.screen, (0, 255, 0), self.player.rect, 1)
                    pygame.draw.rect(self.screen, (0, 0, 255), self.player.death_rect, 2)
                    
                    for obs in self.level_manager.obstacles:
                        pygame.draw.rect(self.screen, (255, 0, 0), obs.rect, 1)

            self.ui.draw(self.screen, self.state, self.level_manager.attempts, self.level_manager.distance)
            
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
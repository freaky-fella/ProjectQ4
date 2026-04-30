import pygame
from settings import GROUND_Y, SCREEN_HEIGHT, SCREEN_WIDTH, BLACK, WHITE, FPS, CYAN
from player import Player
from levelManager import LevelManager
from gameUI import GameUI
import sys
class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Geometry Dash Clone")
        self.clock = pygame.time.Clock()
        
        self.state = "MENU" # Initial state
        self.player = Player()
        self.level_manager = LevelManager()
        self.ui = GameUI()
    
        # Load menu drawing

        self.menu_image = pygame.image.load("Menu.png").convert_alpha()
        self.menu_image = pygame.transform.scale(self.menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))



        self.bg_image = pygame.image.load("backgroundimage.png").convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bg_x = 0
        self.bg_speed = 2

        # Define button areas for level selection 
        self.level_buttons = {
            1: pygame.Rect(SCREEN_WIDTH // 2 - 100, 250 + (1 * 80), 200, 50),
            2: pygame.Rect(SCREEN_WIDTH // 2 - 100, 250 + (2 * 80), 200, 50),
            3: pygame.Rect(SCREEN_WIDTH // 2 - 100, 250 + (3 * 80), 200, 50)
        }
    
    def check_collisions(self):
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
        if self.player.mode != "WAVE":
            self.player.trail_points = []
    def run(self):
        running = True
        while running:
            self.screen.fill(BLACK) 

            # Background drawing for playing state
            if self.state == "PLAYING" and self.bg_image:
                self.screen.blit(self.bg_image, (self.bg_x, 0))
                self.screen.blit(self.bg_image, (self.bg_x + SCREEN_WIDTH, 0))

            
                         
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        print("C detected!")
                        self.player.swap_avatar()

                if event.type == pygame.MOUSEBUTTONDOWN and self.state == "LEVEL_SELECT":
                    for level_num, rect in self.level_buttons.items():
                        if rect.collidepoint(event.pos):
                            self.level_manager.load_level(level_num) 
                            
                            self.player.mode = "CUBE"
                            self.player.rect.y = GROUND_Y - self.player.size
                            self.player.vel_y = 0
                            self.player.trail_points = []
                            
                            self.state = "PLAYING"
                
                

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        self.level_manager.show_hitboxes = not self.level_manager.show_hitboxes
                    
                    if event.key == pygame.K_SPACE:
                        if self.state == "MENU":
                            self.state = "LEVEL_SELECT" # Transition to selector
                        elif self.state in ["GAMEOVER", "VICTORY"]:
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
                
                self.bg_x -= self.bg_speed 
                if self.bg_x <= -SCREEN_WIDTH:
                    self.bg_x = 0
                
                if self.level_manager.check_win():
                    self.state = "VICTORY"

            # Draw Ground Line
            pygame.draw.line(self.screen, WHITE, (0, GROUND_Y), (SCREEN_WIDTH, GROUND_Y), 2)
            
            
            
            if self.state in ["PLAYING", "GAMEOVER", "VICTORY"]:
                self.player.draw(self.screen)
                for obs in self.level_manager.obstacles: obs.draw(self.screen)
                for plat in self.level_manager.platforms: plat.draw(self.screen)
                for p in self.level_manager.portals: p.draw(self.screen)

            self.ui.draw(self.screen, self.state, self.level_manager.attempts, 
                         self.level_manager.distance, self.menu_image)
            
            if self.player.mode == "WAVE" and len(self.player.trail_points) > 1:
                pygame.draw.lines(self.screen, (0, 255, 255), False, self.player.trail_points, 3)

            if self.state == "PLAYING" or self.state == "GAMEOVER":
                self.player.draw(self.screen)
                            
                self.player.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
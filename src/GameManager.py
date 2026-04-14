
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

    def check_collisions(self):
        for obs in self.level_manager.obstacles:
            if self.player.rect.colliderect(obs.rect):
                self.state = "GAMEOVER"

    def run(self):
        running = True
        while running:
            self.screen.fill(BLACK)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.state == "MENU" or self.state == "GAMEOVER":
                            self.level_manager.reset()
                            self.state = "PLAYING"

            if self.state == "PLAYING":
                self.player.handle_input()
                self.player.apply_gravity()
                self.level_manager.update()
                self.check_collisions()
                
                # Draw World
                pygame.draw.line(self.screen, WHITE, (0, GROUND_Y), (SCREEN_WIDTH, GROUND_Y), 2)
                self.player.draw(self.screen)
                for obs in self.level_manager.obstacles:
                    obs.draw(self.screen)

            self.ui.draw(self.screen, self.state, self.level_manager.attempts, self.level_manager.distance)
            
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()

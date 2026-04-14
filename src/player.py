import pygame
from settings import GROUND_Y, JUMP_STRENGTH, GRAVITY, CYAN

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, GROUND_Y - 32, 32, 32)
        self.vel_y = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.rect.bottom >= GROUND_Y:
            self.vel_y = JUMP_STRENGTH

    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        
        if self.rect.bottom > GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, CYAN, self.rect)

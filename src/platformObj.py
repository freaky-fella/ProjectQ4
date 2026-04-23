import pygame
from settings import WHITE

class Platform:
    def __init__(self, x, y):
        size = 60
        self.draw_rect = pygame.Rect(x, y, size, size)
        # Adjust internal hitbox for landing logic
        self.rect = pygame.Rect(x + 5, y + 5, size - 10, size - 10) 
        self.speed = 7

    def update(self):
        self.draw_rect.x -= self.speed
        self.rect.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.draw_rect)
        pygame.draw.rect(screen, (150, 150, 150), self.draw_rect, 1)
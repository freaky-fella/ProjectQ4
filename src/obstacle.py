import pygame
from settings import RED, GROUND_Y

class Obstacle:

    def __init__(self, x, y=None):
        size = 60 
        if y is None: y = GROUND_Y - size
        
        self.draw_rect = pygame.Rect(x, y, size, size)
        self.rect = pygame.Rect(x + 15, y + 20, size - 30, size - 25)
        self.speed = 7

    def update(self):
        self.draw_rect.x -= self.speed
        self.rect.x -= self.speed

    def draw(self, screen):
        points = [
            (self.draw_rect.left, self.draw_rect.bottom),
            (self.draw_rect.right, self.draw_rect.bottom),
            (self.draw_rect.centerx, self.draw_rect.top)
        ]
        pygame.draw.polygon(screen, RED, points)
        
    
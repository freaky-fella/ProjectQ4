import pygame
import random
from settings import GROUND_Y, SCREEN_WIDTH, RED

class Obstacle:
    def __init__(self, x):
        self.rect = pygame.Rect(x, GROUND_Y - 30, 30, 30)
        self.speed = 7

    def update(self):
        self.rect.x -= self.speed

    def draw(self, screen):
        points = [
            (self.rect.left, self.rect.bottom),
            (self.rect.right, self.rect.bottom),
            (self.rect.centerx, self.rect.top)
        ]
        pygame.draw.polygon(screen, RED, points)

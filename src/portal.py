import pygame
from settings import SPEED

class Portal:
    def __init__(self, x, y, target_mode):
        self.rect = pygame.Rect(x, y, 100, 150) 
        self.target_mode = target_mode
        self.activated = False

        if target_mode == "WAVE":
            self.image = pygame.image.load("waveportal.png").convert_alpha()
        else:
            self.image = pygame.image.load("cubeportal.png").convert_alpha()
        
        self.image = pygame.transform.scale(self.image, (100, 150))


    def update(self):
        # Move at the exact same speed as spikes and blocks
        self.rect.x -= SPEED

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
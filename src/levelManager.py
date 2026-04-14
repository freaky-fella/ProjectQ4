
import pygame
import random
from settings import GROUND_Y, SCREEN_WIDTH, RED
from obstacle import Obstacle

class LevelManager:
    def __init__(self):
        self.obstacles = []
        self.spawn_timer = 0
        self.attempts = 1
        self.distance = 0

    def update(self):
        self.distance += 1
        self.spawn_timer += 1
        
        if self.spawn_timer > random.randint(60, 120):
            self.obstacles.append(Obstacle(SCREEN_WIDTH))
            self.spawn_timer = 0

        for obs in self.obstacles[:]:
            obs.update()
            if obs.rect.right < 0:
                self.obstacles.remove(obs)

    def reset(self):
        self.obstacles = []
        self.spawn_timer = 0
        self.distance = 0
        self.attempts += 1

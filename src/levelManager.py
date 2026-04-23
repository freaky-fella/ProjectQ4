import pygame
from portal import Portal
from settings import GROUND_Y, SCREEN_WIDTH, SPEED
from obstacle import Obstacle
from platformObj import Platform

class LevelManager:
    def __init__(self):
        self.portals = []
        self.obstacles = []
        self.platforms = []
        self.attempts = 0
        self.distance = 0
        self.show_hitboxes = False # h key for toggle
        
        # format (x, type of obstacle, how high in the air 0= ground or also understand it as input*100 pixels up)
        # type 't' = spiek, 'b' = block
        self.level_data = [

(0, 'p', 1, "CUBE"),

(600, 't', 0), (660, 't', 0), (720, 't', 0),
(935, 'b', 1.5), (1040, 'b', 0), 
(1200, 't', 0), (1800, 't', 0), (2400, 'b', 1), (2460, 'b', 1),
(3200, 't', 0), (3800, 'b', 2), (4500, 't', 0), (5200, 'b', 1),
(6000, 't', 0), (6100, 't', 0), 

(7000, 'b', 0), (7060, 'b', 1), (7120, 'b', 2), (7400, 't', 2),
(8000, 'b', 1.5), (8100, 't', 1.5), (8600, 'b', 0), (8660, 'b', 0),
(9200, 't', 0.5), (9800, 'b', 3), (10500, 't', 0), (11000, 'b', 1),

(13500, 't', 0), (13580, 't', 0), (13660, 't', 0),
(14200, 'b', 2), (14260, 't', 2), (14500, 'b', 0), (14560, 't', 0),
(15200, 'b', 1), (15300, 'b', 2), (15400, 'b', 3), (15500, 't', 3),
(16200, 't', 0), (16300, 'b', 1), (16400, 't', 1), (17000, 'b', 0),

(19000, 't', 0), (19800, 'b', 4), (20000, 't', 4),
(21500, 'b', 1.5), (22500, 't', 0), (23500, 'b', 0.5),
(24500, 'b', 2.5), (25500, 't', 0), (26500, 'b', 1),
(27000, 't', 0) 
]
        self.spawned_indices = []

    def update(self):
        self.distance += SPEED 
        for i, data in enumerate(self.level_data):
            if self.distance >= data[0] and i not in self.spawned_indices:
                spawn_x = SCREEN_WIDTH
                obj_type = data[1]
                level = data[2]
                y_pos = GROUND_Y - (level * 60) 

                if obj_type == 'p':
                    target_mode = data[3]
                    self.portals.append(Portal(spawn_x, y_pos - 100, target_mode))
                elif obj_type == 't':
                    self.obstacles.append(Obstacle(spawn_x, y_pos - 60))
                elif obj_type == 'b':
                    self.platforms.append(Platform(spawn_x, y_pos - 60))
                
                self.spawned_indices.append(i)
        for p in self.portals[:]:
            p.update()
            if p.rect.right < 0: self.portals.remove(p)
        for obs in self.obstacles[:]:
            obs.update()
            if obs.rect.right < 0: self.obstacles.remove(obs)
        for plat in self.platforms[:]:
            plat.update()
            if plat.rect.right < 0: self.platforms.remove(plat)

    def draw(self, screen):
        for p in self.portals:
            p.draw(screen)
            
        for plat in self.platforms:
            plat.draw(screen)
            
        for obs in self.obstacles:
            obs.draw(screen)
    def check_win(self):
        if self.level_data:
            return self.distance > self.level_data[-1][0] + 2000
        return False

    def reset(self):
        self.obstacles = []
        self.platforms = []
        self.spawned_indices = []
        self.distance = 0
        self.attempts += 1
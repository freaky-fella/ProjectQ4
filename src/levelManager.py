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
        self.show_hitboxes = False 
        self.spawned_indices = []

        # All your levels stored in a dictionary
        # Format: (x_position, type, height_multiplier, [optional mode for portals])
        self.levels = {
            1: [
                (0, 'p', 1, "CUBE"),
                (600, 't', 0), (660, 't', 0), (720, 't', 0),
                (935, 'b', 1.5), (1040, 'b', 0), 
                (1200, 't', 0), (1800, 't', 0), (2400, 'b', 1), (2460, 'b', 1),
                (3200, 't', 0), (3800, 'b', 2), (4500, 't', 0), (5200, 'b', 1),
                (6000, 't', 0), (6100, 't', 0), (7000, 'b', 0), (8000, 't', 0)
            ],
            2: [
                (0, 'p', 1, "CUBE"),
                (800, 'b', 0), (860, 'b', 0), (920, 'b', 0), 
                (1500, 't', 0), (2000, 't', 0), (2060, 't', 0), 
                (3000, 'b', 0), (3060, 'b', 0), (3120, 't', 1), 
                (4500, 'b', 0), (4800, 'b', 2), (5100, 'b', 0), 
                

                (6500, 'p', 3, "WAVE"), 

                
                (10840, 't',6), (10900, 't',6), (10960, 't',6), (11000, 't',6),
                (11000, 'p', 3, "CUBE"),
                (13120, 't',0), (13180, 't',0), (13240, 't', 0), (13300, 't',0)
            ],
            3: [
                (0, 'p', 1, "CUBE"),(0,'b',3),(0,'b',4),(0,'b',5),(0,'b',6),(0,'b',7),(0,'b',8),(0,'b',9),(0,'b',10),(0,'b',11),(0,'b',12),
                (1000, 'b', 0), (1060, 't', 1), (1120, 'b', 0), 
                (2500, 't', 0), (2560, 't', 0), (3500, 'b', 0), (3560, 't', 0), 
                (5000, 't', 0), (5060, 't', 0), (5120, 't', 0), 
                
                (5600, 'b', 0), (5660, 'b', 0),
                (5800, 'b', 1), (5860, 'b', 1),
                (6000, 'b', 2), (6060, 'b', 2),
                
                (6600, 'b', 0), (6600, 'b',1),

                (7000, 'b', 4), (7000,'t',3),(7000,'t',2),(7000,'t',1),

                (7200, 't', 0), (7260, 't', 0), (7320, 't', 0),

                (7500, 't', 0), (7560, 't', 0), (7620, 't', 0),

                

                (10000, 'p', 2, "WAVE"), (10060, 't', 0),
                
                (10200, 'b', 2), (10200, 'b', 6),
                (10260, 'b', 2), (10260, 'b', 6),
                (10320, 'b', 2), (10320, 'b', 6),
                (10380, 'b', 2), (10380, 'b', 6),
                (10440, 'b', 2), (10440, 'b', 6),
                (10500, 'b', 2), (10500, 'b', 6),
                (10560, 'b', 2), (10560, 'b', 6),
                (10620, 'b', 2), (10620, 'b', 6),
                (10680, 'b', 2), (10680, 'b', 6),
                (10740, 'b', 2), (10740, 'b', 6),
                (10800, 'b', 2), (10800, 'b', 6),
                (10860, 'b', 2), (10860, 'b', 6),
                (10920, 'b', 2), (10920, 'b', 6),
                (10980, 'b', 2.5), (10980, 'b', 5.5),
                (11040, 'b', 2.5), (11040, 'b', 5.5),
                (11100, 'b', 2.5), (11100, 'b', 5.5),
                (11160, 'b', 2.5), (11160, 'b', 5.5),
                (11220, 'b', 2.5), (11220, 'b', 5.5),
                (11280, 'b', 2.5), (11280, 'b', 5.5),
                (11340, 'b', 2.5), (11340, 'b', 5.5),
                (11400, 'b', 2.5), (11400, 'b', 5.5),
                (11460, 'b', 2.5), (11460, 'b', 5.5),
                (11520, 'b', 2.5), (11520, 'b', 5.5),
                (11580, 'b', 2.5), (11580, 'b', 5.5),
                (11640, 'b', 2.5), (11640, 'b', 5.5),
                (11700, 'b', 2.5), (11700, 'b', 5.5),
                (11760, 'b', 2.5), (11760, 'b', 5.5),
                (11820, 'b', 2.5), (11820, 'b', 5.5),
                (11880, 'b', 2.5), (11880, 'b', 5.5),
                (11940, 'b', 2.5), (11940, 'b', 5.5),
                (12000, 'b', 2.5), (12000, 'b', 5.5),

                (14000, 'p', 4, "CUBE"),
                (15000, 'b', 0), (15060, 'b', 0), (15120, 'b', 0),
                (15500, 't', 1), (16000, 't', 1), (16500, 't', 1),   
                (18000, 'b', 0) 
            ]
        }
        for x in range(6700, 10840, 60):
            self.levels[2].append((x, 't', 1)) 
            self.levels[2].append((x, 't', 7)) 
            
        for x in range(11000, 12560, 60):
            self.levels[2].append((x, 'b', 0)) 
            self.levels[2].append((x, 'b', 4)) 
        
        self.levels[2].sort(key=lambda x: x[0])

        self.level_data = self.levels[1]

    def load_level(self, level_number):
        """Swaps the current level data and restarts the progress."""
        if level_number in self.levels:
            self.level_data = self.levels[level_number]
            self.reset()

    def reset(self):
        """Clears all active objects and resets distance for redo."""
        self.obstacles = []
        self.platforms = []
        self.portals = []
        self.spawned_indices = []
        self.distance = 0
        self.attempts += 1

    def update(self):
        self.distance += SPEED
        
        # Spawn logic
        for i, data in enumerate(self.level_data):
            if i not in self.spawned_indices and self.distance >= data[0]:
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

        # Update and remove off-screen objects
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
        for p in self.portals: p.draw(screen)
        for plat in self.platforms: plat.draw(screen)
        for obs in self.obstacles: obs.draw(screen)

    def check_win(self):
        if self.level_data:
            return self.distance > self.level_data[-1][0] + 5000
        return False
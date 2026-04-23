import pygame
from settings import GROUND_Y, JUMP_STRENGTH, GRAVITY

class Player:
    def __init__(self):
        size=60
        try:
            self.image = pygame.image.load("player_icon.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (size, size))
        except:
            self.image = pygame.Surface((size, size))
            self.image.fill((0, 255, 255))

        self.rect = pygame.Rect(100, GROUND_Y - size, size, size)
        

        self.death_rect = pygame.Rect(0, 0, size-20, size-20)
        
        self.vel_y = 0
        self.angle = 0
        self.on_ground = True
        self.mode="CUBE"
        self.wave_speed=7
        self.trail_points = []
        
    def apply_gravity(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        
        self.death_rect.center = self.rect.center
        
        if not self.on_ground:
            self.angle -= 7
        else:
            self.angle = round(self.angle / 90) * 90

        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.on_ground = True

    def handle_input(self):
            keys = pygame.key.get_pressed()
            mousebuttons = pygame.mouse.get_pressed()
            self.is_pressing = keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w] or mousebuttons[0]
            
            if self.mode == "CUBE":
                if self.is_pressing and (self.on_ground or self.coyote_timer > 0):
                    self.vel_y = JUMP_STRENGTH
                    self.on_ground = False
                    self.coyote_timer = 0 

    def apply_wave_physics(self):
        if self.is_pressing:
            self.vel_y = -self.wave_speed 
            self.angle = 45
        else:
            self.vel_y = self.wave_speed  
            self.angle = -45
            
        self.rect.y += self.vel_y
        self.death_rect.center = self.rect.center
        
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
        if self.rect.top <= 0:
            self.rect.top = 0
        self.trail_points.append(list(self.rect.center))

        for point in self.trail_points:
            point[0] -= 7 

        self.trail_points = [p for p in self.trail_points if p[0] > -10]
    def apply_physics(self):
        if self.mode == "WAVE":
            self.apply_wave_physics()
        else:
            self.apply_gravity()
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, new_rect.topleft)
        self.trail_points.append(list(self.rect.center))

        for point in self.trail_points:
            point[0] -= 7 

        self.trail_points = [p for p in self.trail_points if p[0] > -10]
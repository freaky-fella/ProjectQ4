import pygame
from settings import GROUND_Y, JUMP_STRENGTH, GRAVITY

class Player:
    def __init__(self):
        self.size=60

        try:
            self.image = pygame.image.load("player_icon.png").convert_alpha()
        except:
            # Fallback if file is missing
            self.image = pygame.Surface((self.size, self.size))
            self.image.fill((0, 255, 255))

        self.avatar1 = pygame.transform.scale(self.image, (self.size, self.size))
        
        try:
            alt_img = pygame.image.load("avatar2.png").convert_alpha()
            self.avatar2 = pygame.transform.scale(alt_img, (self.size, self.size))
        except:
            self.avatar2 = pygame.Surface((self.size, self.size))
            self.avatar2.fill((255, 0, 255)) 

        self.image = self.avatar2 
        
        self.rect = self.image.get_rect(topleft=(100, GROUND_Y - self.size))
        

        self.death_rect = pygame.Rect(0, 0, self.size-20, self.size-20)
        
        self.vel_y = 0
        self.angle = 0
        self.on_ground = True
        self.mode="CUBE"
        self.wave_speed=7
        self.trail_points = []
    
    def load_avatar(self, filename):
        try:
            img = pygame.image.load(filename).convert_alpha()
            return pygame.transform.scale(img, (self.size, self.size))
        except:
            # Fallback if image is missing
            surf = pygame.Surface((self.size, self.size))
            surf.fill((0, 255, 255) if "alt" not in filename else (255, 0, 255))
            return surf

    def swap_avatar(self):
        if self.image == self.avatar1:
            self.image = self.avatar2
            print("Switched to Avatar 2")
        else:
            self.image = self.avatar1
            print("Switched to Avatar 1")

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

        # Add the current center to the trail
        self.trail_points.append(list(self.rect.center))

        # Move trail points left to match level speed (7px)
        for point in self.trail_points:
            point[0] -= 7 


        if len(self.trail_points) > 200:
            self.trail_points.pop(0)

    def draw(self, screen):
        # This uses whatever the current 'self.image' is
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, new_rect.topleft)


    def apply_physics(self):
        if self.mode == "WAVE":
            self.apply_wave_physics()
        else:
            self.apply_gravity()

        for point in self.trail_points:
            point[0] -= 7 

        self.trail_points = [p for p in self.trail_points if p[0] > -10]
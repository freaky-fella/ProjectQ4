import pygame
from settings import WHITE, RED, SCREEN_WIDTH, SCREEN_HEIGHT

class GameUI:
    def __init__(self):
        # Standard and Title fonts
        self.font = pygame.font.SysFont("Arial", 24)
        self.large_font = pygame.font.SysFont("Arial", 48, bold=True)

    def draw(self, screen, state, attempts, distance, menu_img=None):
        if state == "MENU":
            if menu_img:
                # Draw your custom drawing
                screen.blit(menu_img, (0, 0))
            else:
                # Fallback text
                text = self.font.render("BAD GEOMETRY DASH - Press SPACE to Start", True, WHITE)
                screen.blit(text, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2))
        
        elif state == "LEVEL_SELECT":
            # level selection buttons
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180)) 
            screen.blit(overlay, (0, 0))

            title = self.large_font.render("SELECT A LEVEL: 1 is easy 2 and 3 are harder", True, WHITE)
            screen.blit(title, (SCREEN_WIDTH // 2 - 400, 150))

            # Draw 3 Level Buttons
            for i in range(1, 4):
                button_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, 250 + (i * 80), 200, 50)
                pygame.draw.rect(screen, WHITE, button_rect, 2, border_radius=10)
                
                lvl_text = self.font.render(f"LEVEL {i}", True, WHITE)
                text_rect = lvl_text.get_rect(center=button_rect.center)
                screen.blit(lvl_text, text_rect)

        elif state == "PLAYING":
            attempt_text = self.font.render(f"Attempt {attempts}", True, WHITE)
            dist_text = self.font.render(f"Progress: {distance // 10}", True, WHITE)
            screen.blit(attempt_text, (20, 20))
            screen.blit(dist_text, (SCREEN_WIDTH - 300, 20))

        elif state == "GAMEOVER":
            text = self.font.render("CRASHED! Press SPACE to Try Again", True, RED)
            screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))

        elif state == "VICTORY":
            win_text = self.font.render("LEVEL COMPLETE!", True, (255, 215, 0))
            sub_text = self.font.render("Press SPACE to Play Again", True, WHITE)
            screen.blit(win_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))
            screen.blit(sub_text, (SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 + 20))
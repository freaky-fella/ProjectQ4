import pygame
from settings import WHITE, RED, SCREEN_WIDTH, SCREEN_HEIGHT

class GameUI:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 24)

    def draw(self, screen, state, attempts, distance):
        if state == "MENU":
            text = self.font.render("BAD GEOMETRY DASH - Press SPACE to Start", True, WHITE)
            screen.blit(text, (SCREEN_WIDTH//2 - 180, SCREEN_HEIGHT//2))
        
        elif state == "PLAYING":
            attempt_text = self.font.render(f"Attempt {attempts}", True, WHITE)
            dist_text = self.font.render(f"Progress: {distance // 10}", True, WHITE)
            screen.blit(attempt_text, (20, 20))
            screen.blit(dist_text, (SCREEN_WIDTH - 150, 20))

        elif state == "GAMEOVER":
            text = self.font.render("CRASHED! Press SPACE to Try Again", True, RED)
            screen.blit(text, (SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2))
        elif state == "VICTORY":
            win_text = self.font.render("LEVEL COMPLETE!", True, (255, 215, 0))
            sub_text = self.font.render("Press SPACE to Play Again", True, WHITE)
            screen.blit(win_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 20))
            screen.blit(sub_text, (SCREEN_WIDTH//2 - 130, SCREEN_HEIGHT//2 + 20))

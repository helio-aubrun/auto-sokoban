import pygame
import sys
from game import Game
from utils import draw_text

class MainMenu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.background_img = pygame.image.load("images/background.webp")

    def run(self):
        font_large = pygame.font.Font(None, 100)
        click = False
        
        while True:
            self.screen.blit(self.background_img, (0, 0))
            
            mx, my = pygame.mouse.get_pos()
            start_button_rect = pygame.Rect(450, 300, 300, 75)
            
            if start_button_rect.collidepoint((mx, my)) and click:
                self.start_game()
            
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            
            pygame.display.flip()

    def start_game(self):
        level = 1
        while level:
            game = Game(self.screen, self.width, self.height, 40, level)
            level = game.run()
        self.show_victory_screen()

    def show_victory_screen(self):
        font_large = pygame.font.Font(None, 100)
        click = False
        
        while True:
            self.screen.fill((255, 255, 255))
            draw_text(self.screen, 'You Win!', font_large, (0, 0, 0), self.width // 2, self.height // 3)
            
            mx, my = pygame.mouse.get_pos()
            retry_button = pygame.Rect(self.width // 2 - 150, self.height // 2 + 75, 300, 75)
            main_menu_button = pygame.Rect(self.width // 2 - 150, self.height // 2 + 175, 300, 75)
            
            if retry_button.collidepoint((mx, my)):
                pygame.draw.rect(self.screen, (173, 216, 230), retry_button)
                if click:
                    self.start_game()
            else:
                pygame.draw.rect(self.screen, (0, 0, 255), retry_button)
                
            if main_menu_button.collidepoint((mx, my)):
                pygame.draw.rect(self.screen, (173, 216, 230), main_menu_button)
                if click:
                    self.run()
            else:
                pygame.draw.rect(self.screen, (0, 0, 255), main_menu_button)
            
            draw_text(self.screen, 'Retry', font_large, (0, 0, 0), self.width // 2, self.height // 2 + 112)
            draw_text(self.screen, 'Main Menu', font_large, (0, 0, 0), self.width // 2, self.height // 2 + 212)
            
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            
            pygame.display.flip()

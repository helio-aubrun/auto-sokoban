import pygame
import sys
from game import Game

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
            game = Game(self.screen, self.width, self.height, 20, level)
            level = game.run()
        self.show_victory_screen()
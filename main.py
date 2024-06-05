import pygame
from menu import MainMenu

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
TILESIZE = 40

# Initialisation de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sokoban Game")

def main():
    main_menu = MainMenu(screen, WIDTH, HEIGHT)
    main_menu.run()

if __name__ == "__main__":
    main()
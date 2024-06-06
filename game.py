import pygame
import sys
from map import Map

class Game:
    def __init__(self, screen, width, height, tilesize, level):
        self.screen = screen
        self.width = width
        self.height = height
        self.tilesize = tilesize
        self.level = level
        self.grid_width = width // tilesize
        self.grid_height = height // tilesize
        self.map = Map(self.grid_width, self.grid_height, self.tilesize, level)
        self.font = pygame.font.Font(None, 36)

    def draw_grid(self):
        for y in range(self.grid_height - 8):
            for x in range(self.grid_width):
                rect = pygame.Rect(x * self.tilesize, y * self.tilesize, self.tilesize, self.tilesize)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

    def run(self):
        running = True
        while running:
            self.screen.fill((255, 255, 255))
            self.draw_grid()
            self.map.draw_level(self.screen)
            self.draw_retry_button()

            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.map.move_player(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.map.move_player(1, 0)
                    elif event.key == pygame.K_UP:
                        self.map.move_player(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.map.move_player(0, 1)
                    elif event.key == pygame.K_u:
                        self.map.undo_move()
                    elif event.key == pygame.K_r:
                        self.map.reset_game(self.level)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.retry_button_rect.collidepoint((mx, my)):
                            self.map.reset_game(self.level)

            if self.map.win:
                return self.level + 1 if self.level < 3 else 0

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def draw_retry_button(self):
        retry_img = pygame.image.load("images/retry.png")
        self.retry_button_rect = pygame.Rect(self.width // 2 - 100, self.height - 140, 200, 80)
        self.screen.blit(retry_img, (self.width // 2 - retry_img.get_width() // 2, self.height - 160))
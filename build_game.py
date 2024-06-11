import pygame
import sys
from pygame.locals import *
from display_game import DisplayGame
from ia import IA

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        width = 600
        height = 700
        self.block_size = 60
        self.block_number = width // self.block_size
        self.screen = pygame.display.set_mode((width, height))
        pygame.mixer.music.load("music/song.mp3")
        self.volume = 0.1
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)
        self.map = [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 4, 2, 0, 0, 0, 0, 0, 0, 5],
            [5, 5, 5, 0, 1, 0, 0, 5, 5, 5],
            [5, 4, 5, 0, 0, 4, 0, 5, 5, 5],
            [5, 0, 5, 0, 0, 0, 0, 0, 5, 5],
            [5, 2, 5, 0, 0, 2, 0, 0, 5, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 5, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        ]
        self.player_x, self.player_y = 4, 2
        self.score = 0
        self.nb_coup = 0
        self.score_pos = (0, 630)
        self.font = pygame.font.SysFont(None, 36)
        self.max_score = sum(row.count(4) for row in self.map)
        self.max_score_pos = (300, 630)
        self.game_states = []
        self.display = DisplayGame(self)
        self.use_ia = False
        self.ia = IA(self)

    def signaler_mouvement(self):
        self.nb_coup += 1

    def reset_game(self):
        self.player_x, self.player_y = 4, 2
        self.score = 0
        self.nb_coup = 0
        self.use_ia = False
        self.map = [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 4, 2, 0, 0, 0, 0, 0, 0, 5],
            [5, 5, 5, 0, 1, 0, 0, 5, 5, 5],
            [5, 4, 5, 0, 0, 4, 0, 5, 5, 5],
            [5, 0, 5, 0, 0, 0, 0, 0, 5, 5],
            [5, 2, 5, 0, 0, 2, 0, 0, 5, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 5, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        ]
        self.game_states.clear()
        pygame.display.flip()

    def moving(self, change_x, change_y, map):
        current_state = {
            'player_x': self.player_x,
            'player_y': self.player_y,
            'map': [row[:] for row in self.map]
        }
        self.game_states.append(current_state)

        temp_x = self.player_x + change_x
        temp_y = self.player_y + change_y

        if self.map[temp_y][temp_x] == 0:
            if self.map[self.player_y][self.player_x] == 6:
                self.map[self.player_y][self.player_x] = 4
            else:
                self.map[self.player_y][self.player_x] = 0
            self.player_x = temp_x
            self.player_y = temp_y
            self.map[self.player_y][self.player_x] = 1
        elif self.map[temp_y][temp_x] == 4:
            if self.map[self.player_y][self.player_x] == 6:
                self.map[self.player_y][self.player_x] = 4
            else:
                self.map[self.player_y][self.player_x] = 0
            self.player_x = temp_x
            self.player_y = temp_y
            self.map[self.player_y][self.player_x] = 6
        elif self.map[temp_y][temp_x] == 2 and self.map[temp_y + change_y][temp_x + change_x] == 0:
            self.map[self.player_y][self.player_x] = 0
            self.player_x = temp_x
            self.player_y = temp_y
            self.map[self.player_y][self.player_x] = 1
            self.map[temp_y + change_y][temp_x + change_x] = 2
        elif self.map[temp_y][temp_x] == 2 and self.map[temp_y + change_y][temp_x + change_x] == 4:
            if self.map[self.player_y][self.player_x] == 6:
                self.map[self.player_y][self.player_x] = 4
            else:
                self.map[self.player_y][self.player_x] = 0
            self.player_x = temp_x
            self.player_y = temp_y
            self.map[self.player_y][self.player_x] = 1
            self.map[temp_y + change_y][temp_x + change_x] = 3
            self.score += 1
        else:
            return False

    def run(self):
        running = True
        fin = False
        while running:
            if not fin :
                while not (self.score == self.max_score):
                    for event in pygame.event.get():
                        self.display.update_display()
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_t:
                                self.use_ia = True
                            elif event.key == pygame.K_e:
                                if len(self.game_states) > 1:
                                    previous_state = self.game_states.pop()
                                    self.player_x, self.player_y = previous_state['player_x'], previous_state['player_y']
                                    self.map = previous_state['map']
                            elif event.key == pygame.K_ESCAPE:
                                running = False
                                pygame.quit()
                                sys.exit()
                            elif event.key == pygame.K_r:
                                self.reset_game()
                            elif event.key == pygame.K_UP or event.key == ord('z'):
                                self.nb_coup += 1
                                self.moving(0, -1, self.map)
                            elif event.key == pygame.K_DOWN or event.key == ord('s'):
                                self.nb_coup += 1
                                self.moving(0, 1, self.map)
                            elif event.key == pygame.K_LEFT or event.key == ord('q'):
                                self.nb_coup += 1
                                self.moving(-1, 0, self.map)
                            elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                                self.nb_coup += 1
                                self.moving(1, 0, self.map)
                            self.display.update_display()

                    if self.use_ia:
                        self.ia.make_move()
                        self.display.update_display()
                        pygame.time.wait(300)
            if (self.score == self.max_score) :
                fin = True

            self.display.display_victory()
            for event in pygame.event.get():
                self.display.update_display()
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        self.score = 0
                        fin = False
                          # Sortir de la boucle pour éviter de redémarrer le jeu plusieurs fois
        running = False

        pygame.quit()
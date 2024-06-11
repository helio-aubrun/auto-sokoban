# display_game.py

import pygame

class DisplayGame:
    def __init__(self, game):
        width = 600
        heidth = 700
        self.game = game
        self.screen = game.screen
        self.block_size = game.block_size
        self.block_number = game.block_number
        self.fond_img = pygame.transform.scale(pygame.image.load("images/0.jpg"), (width // self.block_number, width // self.block_number))
        self.mur_img = pygame.transform.scale(pygame.image.load("images/5jjk.png"), (width // self.block_number, width // self.block_number))

        # block_np
        self.block_np_img = pygame.transform.scale(pygame.image.load("images/2jjk.png"), (width // self.block_number, width // self.block_number))

        # block_pl
        self.block_pl_img = pygame.transform.scale(pygame.image.load("images/boxe_close_antic.png"), (width // self.block_number, width // self.block_number))

        # jouer
        self.jouer_img = pygame.transform.scale(pygame.image.load("images/1jjk.png"), (width // self.block_number, width // self.block_number))

        # emplacement
        self.emplacement_img = pygame.transform.scale(pygame.image.load("images/boxe_open_antic.png"), (width // self.block_number, width // self.block_number))
        self.font = game.font
        self.score_pos = game.score_pos
        self.max_score_pos = game.max_score_pos
        self.max_score = game.max_score

    def update_display(self):
        self.screen.fill((245, 245, 245))
        for i in range(self.block_number):
            for j in range(self.block_number):
                self.screen.blit(self.fond_img, (i * self.block_size, j * self.block_size))

        x, y = 0, 0
        for ligne in self.game.map:
            for colmn in ligne:
                if colmn == 0:
                    self.screen.blit(self.fond_img, (x, y))
                elif colmn == 1:
                    self.screen.blit(self.jouer_img, (x, y))
                elif colmn == 2:
                    self.screen.blit(self.block_np_img, (x, y))
                elif colmn == 3:
                    self.screen.blit(self.block_pl_img, (x, y))
                elif colmn == 4:
                    self.screen.blit(self.emplacement_img, (x, y))
                elif colmn == 6:
                    self.screen.blit(self.emplacement_img, (x, y))
                    self.screen.blit(self.jouer_img, (x, y))
                else:
                    self.screen.blit(self.mur_img, (x, y))
                x += self.block_size
            y += self.block_size
            x = 0

        self.aff_score()
        pygame.display.flip()

    def aff_score(self):
        score_render = self.font.render("score : " + str(self.game.nb_coup), True, (0, 0, 0))
        self.screen.blit(score_render, self.score_pos)

    def display_victory(self):
        self.screen.fill((245, 245, 245))
        message = self.font.render("Vous avez gagné", True, (0, 0, 0))
        score = self.font.render("Score : " + str(self.game.nb_coup), True, (0, 0, 0))
        self.screen.blit(message, (200, 200))
        self.screen.blit(score, (200, 250))

        # Texte pour relancer le jeu
        restart_text = self.font.render("R pour rejouer", True, (0, 0, 0))
        self.screen.blit(restart_text, (200, 300))

        pygame.display.flip()

import pygame
import sys
from pygame.locals import *

class main():
    def __init__ (self) :

        # Initialize Pygame
        pygame.init()
        pygame.mixer.init()

        # Set up the display surface
        width = 600
        heidth = 700
        self.block_size = 60 #muste be a devider of 600
        self.block_number =  width //  self.block_size
        self.screen = pygame.display.set_mode((width, heidth))

        pygame.mixer.music.load("music/song.mp3")
        self.volume = 0.1  # Volume à 50%
        pygame.mixer.music.set_volume(self.volume)
        # Démarrer la lecture de la musique
        pygame.mixer.music.play(-1)

        #map
        self.map = [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 4, 2, 0, 0, 0, 0, 0, 0, 5],
            [5, 5, 5, 5, 1, 0, 2, 5, 5, 5],
            [5, 4, 0, 5, 0, 4, 0, 5, 5, 5],
            [5, 0, 0, 5, 0, 0, 0, 0, 5, 5],
            [5, 0, 2, 5, 0, 0, 0, 0, 5, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 5, 5],
            [5, 0, 0, 2, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 4, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        ]

        #mur
        self.mur_img = pygame.transform.scale(pygame.image.load("images/5jjk.png"), (width // self.block_number, width // self.block_number))

        #block_np
        self.block_np_img = pygame.transform.scale(pygame.image.load("images/2jjk.png"), (width // self.block_number, width // self.block_number))

        #block_pl
        self.block_pl_img = pygame.transform.scale(pygame.image.load("images/boxe_close_antic.png"), (width // self.block_number, width // self.block_number))

        #jouer
        self.jouer_img = pygame.transform.scale(pygame.image.load("images/1jjk.png"), (width // self.block_number, width // self.block_number))

        #emplacement
        self.emplacement_img = pygame.transform.scale(pygame.image.load("images/boxe_open_antic.png"), (width // self.block_number, width // self.block_number))

        #fond
        self.fond_img = pygame.transform.scale(pygame.image.load("images/0.jpg"), (width // self.block_number, width // self.block_number))

        # Define player position
        self.player_x, self.player_y = 4, 2  # Starting position

        #set score
        self.score = 0
        self.score_pos = (0, 630)
        self.font = pygame.font.SysFont(None, 36)
        self.max_score = 0
        for sublist in self.map:
            self.max_score += sublist.count(4)
        self.max_score_pos = (300, 630)
        # set last player move
        self.game_states = []

    def reset_game(self):
        # Réinitialise la position du joueur
        self.player_x, self.player_y = 4, 2  # Position de départ
        
        # Réinitialise le score
        self.score = 0
        
        # Réinitialise la carte si nécessaire
        self.map = [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 4, 2, 0, 0, 0, 0, 0, 0, 5],
            [5, 5, 5, 5, 1, 0, 2, 5, 5, 5],
            [5, 4, 0, 5, 0, 4, 0, 5, 5, 5],
            [5, 0, 0, 5, 0, 0, 0, 0, 5, 5],
            [5, 0, 2, 5, 0, 0, 0, 0, 5, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 5, 5],
            [5, 0, 0, 2, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 4, 5],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        ]
        
        # Réinitialise l'historique des états
        self.game_states.clear()

        # Réactualise l'affichage
        pygame.display.flip()


    def aff_score(self):

        score_render = self.font.render("score : " + str(self.score), True, (0, 0, 0))
        
        self.screen.blit(score_render, self.score_pos)

        max_score_render = self.font.render("score max : " + str(self.max_score), True, (0, 0, 0))

        self.screen.blit(max_score_render, self.max_score_pos)
        


    def moving(self,change_x, change_y, map):

        current_state = {
        'player_x': self.player_x,
        'player_y': self.player_y,
        'map': [row[:] for row in self.map]  # Crée une copie superficielle de la liste pour éviter de modifier l'origine
        }
        self.game_states.append(current_state)

        temp_x = self.player_x + change_x
        temp_y = self.player_y + change_y
        
        if self.map[temp_y][temp_x] == 0:
            #pour de placement sur case de but
            if self.map [self.player_y] [self.player_x] == 6 :
                self.map [self.player_y] [self.player_x] = 4
            else :
                self.map [self.player_y] [self.player_x] = 0
            #deplacement vers la nouvel case
            self.player_x = temp_x
            self.player_y = temp_y
            self.map [self.player_y] [self.player_x] = 1
        elif self.map[temp_y][temp_x] == 4:
            #pour de placement sur case de but
            if self.map [self.player_y] [self.player_x] == 6 :
                self.map [self.player_y] [self.player_x] = 4
            else :
                self.map [self.player_y] [self.player_x] = 0
            #deplacement vers la nouvel case
            self.player_x = temp_x
            self.player_y = temp_y
            self.map [self.player_y] [self.player_x] = 6
        elif self.map [temp_y][temp_x] == 2 and self.map [temp_y + change_y][temp_x + change_x] == 0:
            #deplacement vers la nouvel case
            self.map [self.player_y] [self.player_x] = 0
            self.player_x = temp_x
            self.player_y = temp_y
            self.map [self.player_y] [self.player_x] = 1
            #deplacement de lobjet
            self.map [temp_y + change_y][temp_x + change_x] = 2
        elif self.map [temp_y][temp_x] == 2 and self.map [temp_y + change_y][temp_x + change_x] == 4:
            #pour de placement sur case de but
            if self.map [self.player_y] [self.player_x] == 6 :
                self.map [self.player_y] [self.player_x] = 4
            else :
                self.map [self.player_y] [self.player_x] = 0
            #deplacement de 
            self.player_x = temp_x
            self.player_y = temp_y
            self.map [self.player_y] [self.player_x] = 1
            #marquer un point
            self.map [temp_y + change_y][temp_x + change_x] = 3
            self.score += 1
        else:
            return False
        
    def run (self):
        # Main loop
        running = True

        while running:
            while not (self.score == self.max_score) :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.KEYDOWN:
                        # Check for arrow keys or WASD keys
                        if event.key == pygame.K_e:  # Utiliser la touche Echap comme bouton de retour en arrière
                            if len(self.game_states) > 1:
                                previous_state = self.game_states.pop()
                                self.player_x, self.player_y = previous_state['player_x'], previous_state['player_y']
                                self.map = previous_state['map']  # Mettre à jour la carte avec l'état précédent
                        elif event.key == pygame.K_ESCAPE:
                            running = False
                        elif event.key == pygame.K_r:  # Utiliser la touche R comme bouton de réinitialisation
                            self.reset_game()
                        elif event.key == pygame.K_UP or event.key == ord('z'):
                            self.moving (change_x = 0, change_y = -1, map = map)
                        elif event.key == pygame.K_DOWN or event.key == ord('s'):
                            self.moving (change_x = 0, change_y = 1, map = map)
                        elif event.key == pygame.K_LEFT or event.key == ord('q'):
                            self.moving (change_x = -1, change_y = 0, map = map)
                        elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                            self.moving (change_x = 1, change_y = 0, map = map)

                # Clear the screen
                self.screen.fill((245, 245, 245))



                for i in range (self.block_number) :
                    for j in range (self.block_number) :
                        self.screen.blit (self.fond_img, (i * self.block_size, j * self.block_size))

                #affichage de la matrice avec des sprite
                x, y = 0, 0
                for ligne in self.map :
                    for colmn in ligne :
                        if colmn == 0:
                            self.screen.blit (self.fond_img, (x, y))
                        elif colmn == 1:
                            self.screen.blit (self.jouer_img, (x, y))
                        elif colmn == 2 :
                            self.screen.blit (self.block_np_img, (x, y))
                        elif colmn == 3 :
                            self.screen.blit (self.block_pl_img, (x, y))
                        elif colmn == 4 :
                            self.screen.blit (self.emplacement_img, (x, y))
                        elif colmn == 6 :
                            self.screen.blit (self.emplacement_img, (x, y))
                            self.screen.blit (self.jouer_img, (x, y))
                        else :
                            self.screen.blit (self.mur_img, (x, y))
                        x += self.block_size
                    y += self.block_size
                    x = 0


                self.aff_score ()

                # Update the display
                pygame.display.flip()

            if self.score == self.max_score :
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                # Clear the screen
                self.screen.fill((245, 245, 245))

                message = self.font.render("Vous avez gagner", True, (0, 0, 0))
                score = self.font.render ("score : " + str (self.score), True, (0, 0, 0))
        
                self.screen.blit (message, (200,200))
                self.screen.blit (score, (200, 250))

                # Update the display
                pygame.display.flip()
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()


    


if __name__ == "__main__":
    game =  main ()
    game.run ()
import pygame
import sys

class main():
    def __init__ (self) :

        # Initialize Pygame
        pygame.init()

        # Set up the display surface
        width = 600
        heidth = 700
        self.block_size = 60 #muste be a devider of 600
        self.block_number =  width //  self.block_size
        self.screen = pygame.display.set_mode((width, heidth))

        #map
        self.map = [
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
            [5, 0, 0, 2, 0, 0, 4, 0, 0, 5],
            [5, 0, 1, 0, 2, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 4, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 5],
            [5, 0, 0, 0, 0, 0, 0, 0, 0, 5],
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
        self.player_x, self.player_y = 2, 2  # Starting position

        #set score
        self.score = 0
        self.score_pos = (0, 630)
        self.score_font = pygame.font.SysFont(None, 36)
        self.max_score = 0
        for sublist in self.map:
            self.max_score += sublist.count(4)
        self.max_score_pos = (300, 630)


    def aff_score(self):

        score_render = self.score_font.render(str(self.score), True, (0, 0, 0))
        
        self.screen.blit(score_render, self.score_pos)

        max_score_render = self.score_font.render(str(self.max_score), True, (0, 0, 0))

        self.screen.blit(max_score_render, self.max_score_pos)
        


    def moving(self,change_x, change_y, map):

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
                        if event.key == pygame.K_UP or event.key == ord('z'):
                            self.moving (change_x = 0, change_y = -1, map = map)
                        elif event.key == pygame.K_DOWN or event.key == ord('s'):
                            self.moving (change_x = 0, change_y = 1, map = map)
                        elif event.key == pygame.K_LEFT or event.key == ord('q'):
                            self.moving (change_x = -1, change_y = 0, map = map)
                        elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                            self.moving (change_x = 1, change_y = 0, map = map)

                # Clear the screen
                self.screen.fill((255,255,255))



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
                self.screen.fill((255,255,255))

                message = self.score_font.render("Vous avez gagner", True, (0, 0, 0))
        
                self.screen.blit(message, (200,200))

                # Update the display
                pygame.display.flip()

        pygame.quit()
        sys.exit()


    


if __name__ == "__main__":
    game =  main ()
    game.run ()


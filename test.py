matrix = [[0 for _ in range(10)] for _ in range(10)]
for i in matrix : 
    print (i, end = ",\n")


def main():
    # Existing initialization and setup code remains unchanged...

    # Define player position
    player_x, player_y = 0, 0  # Starting position

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Check for arrow keys or WASD keys
                if event.key == pygame.K_UP or event.key == ord('w'):
                    # Move up
                    new_y = player_y - block_size
                    if is_valid_move(player_x, new_y, map):
                        player_y -= block_size
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    # Move down
                    new_y = player_y + block_size
                    if is_valid_move(player_x, new_y, map):
                        player_y += block_size
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    # Move left
                    new_x = player_x - block_size
                    if is_valid_move(new_x, player_y, map):
                        player_x -= block_size
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    # Move right
                    new_x = player_x + block_size
                    if is_valid_move(new_x, player_y, map):
                        player_x += block_size

        # Clear the screen
        screen.fill(white)

        # Draw the map and objects
        draw_map_and_objects(screen, map, player_x, player_y)

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

def is_valid_move(x, y, map):
    # Convert coordinates to grid indices
    grid_x = x // block_size
    grid_y = y // block_size
    
    # Check if the destination cell is valid
    if map[grid_y][grid_x] in [0, 2]:  # Assuming 0 is empty and 2 is a movable object
        return True
    else:
        return False
    



import pygame
import sys

def main():
    # Existing initialization and setup code remains unchanged...

    # Define player position
    player_x, player_y = 0, 0  # Starting position

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Check for arrow keys or WASD keys
                if event.key == pygame.K_UP or event.key == ord('w'):
                    # Move up
                    new_y = player_y - block_size
                    if is_valid_move(player_x, new_y, map):
                        player_y -= block_size
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    # Move down
                    new_y = player_y + block_size
                    if is_valid_move(player_x, new_y, map):
                        player_y += block_size
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    # Move left
                    new_x = player_x - block_size
                    if is_valid_move(new_x, player_y, map):
                        player_x -= block_size
                elif event.key == pygame.K_RIGHT or event.key == ord('d'):
                    # Move right
                    new_x = player_x + block_size
                    if is_valid_move(new_x, player_y, map):
                        player_x += block_size

        # Clear the screen
        screen.fill(white)

        # Draw the map and objects
        draw_map_and_objects(screen, map, player_x, player_y)

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

def is_valid_move(x, y, map):
    # Convert coordinates to grid indices
    grid_x = x // block_size
    grid_y = y // block_size
    
    # Check if the destination cell is valid
    if map[grid_y][grid_x] in [0, 2]:  # Assuming 0 is empty and 2 is a movable object
        return True
    else:
        return False

def draw_map_and_objects(screen, map, player_x, player_y):
    # Existing drawing code...
    pass  # Replace with existing drawing code

if __name__ == "__main__":
    main()



import pygame
import sys

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display surface
    width = 600
    heidth = 700
    block_size = 60 #muste be a devider of 600
    block_number =  width //  block_size
    screen = pygame.display.set_mode((width, heidth))

    #map
    map = [
        [5, 5, 5, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 4, 0, 0, 0],
        [5, 0, 2, 2, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 3, 4, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    #mur
    mur_img = pygame.transform.scale(pygame.image.load("images/5jjk.png"), (width // block_number, width // block_number))

    #block_np
    block_np_img = pygame.transform.scale(pygame.image.load("images/2jjk.png"), (width // block_number, width // block_number))

    #block_pl
    block_pl_img = pygame.transform.scale(pygame.image.load("images/boxe_close_antic.png"), (width // block_number, width // block_number))

    #jouer
    jouer_img = pygame.transform.scale(pygame.image.load("images/1jjk.png"), (width // block_number, width // block_number))

    #emplacement
    emplacement_img = pygame.transform.scale(pygame.image.load("images/boxe_open_antic.png"), (width // block_number, width // block_number))

    #fond
    fond_img = pygame.transform.scale(pygame.image.load("images/0.jpg"), (width // block_number, width // block_number))


    # Define colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white color
        screen.fill(white)

        for i in range (block_number) :
            for j in range (block_number) :
                screen.blit (fond_img, (i * block_size, j * block_size))
        #affichage de la matrice avec des sprite
        x, y = 0, 0
        for ligne in map :
            for colmn in ligne :
                if colmn == 0:
                    screen.blit (fond_img, (x, y))
                elif colmn == 1:
                    screen.blit (jouer_img, (x, y))
                elif colmn == 2 :
                    screen.blit (block_np_img, (x, y))
                elif colmn == 3 :
                    screen.blit (block_pl_img, (x, y))
                elif colmn == 4 :
                    screen.blit (emplacement_img, (x, y))
                else :
                    screen.blit (mur_img, (x, y))
                x += block_size
            y += block_size
            x = 0
                
    

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


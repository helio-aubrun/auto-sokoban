import pygame
import copy
from map_generator import MapGenerator

class Map:
    WALL = MapGenerator.WALL
    EMPTY = MapGenerator.EMPTY
    GOAL = MapGenerator.GOAL
    BOX = MapGenerator.BOX
    BOX_ON_GOAL = MapGenerator.BOX_ON_GOAL

    def __init__(self, grid_width, grid_height, tilesize, level=2):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.tilesize = tilesize
        self.level = MapGenerator.generate(level)
        self.player_pos = [1, 1]
        self.undo_stack = []
        self.win = False

    def draw_level(self, screen):
        player_img = pygame.image.load("images/hélio.jpg")
        box_img = pygame.image.load("images/caisse.jpg")
        goal_img = pygame.image.load("images/étoiles.png")
        wall_img = pygame.image.load("images/mur.jpg")
        box_on_goal_img = pygame.image.load("images/box_on_goal.png")
        
        for y, row in enumerate(self.level):
            for x, tile in enumerate(row):
                if tile == self.WALL:
                    screen.blit(wall_img, (x * self.tilesize, y * self.tilesize))
                elif tile == self.GOAL:
                    screen.blit(goal_img, (x * self.tilesize, y * self.tilesize))
                elif tile == self.BOX:
                    screen.blit(box_img, (x * self.tilesize, y * self.tilesize))
                elif tile == self.BOX_ON_GOAL:
                    screen.blit(box_on_goal_img, (x * self.tilesize, y * self.tilesize))

        x, y = self.player_pos
        screen.blit(player_img, (x * self.tilesize, y * self.tilesize))

    def move_player(self, dx, dy):
        x, y = self.player_pos
        new_x, new_y = x + dx, y + dy

        if self.level[new_y][new_x] == self.WALL:
            return

        if self.level[new_y][new_x] in (self.BOX, self.BOX_ON_GOAL):
            if self.level[new_y + dy][new_x + dx] in (self.EMPTY, self.GOAL):
                self.undo_stack.append(copy.deepcopy(self.level))
                if self.level[new_y + dy][new_x + dx] == self.GOAL:
                    self.level[new_y + dy][new_x + dx] = self.BOX_ON_GOAL
                else:
                    self.level[new_y + dy][new_x + dx] = self.BOX

                if self.level[new_y][new_x] == self.BOX:
                    self.level[new_y][new_x] = self.EMPTY
                elif self.level[new_y][new_x] == self.BOX_ON_GOAL:
                    self.level[new_y][new_x] = self.GOAL

                if self.level[y][x] == self.GOAL:
                    self.level[y][x] = self.GOAL
                else:
                    self.level[y][x] = self.EMPTY

                self.player_pos = [new_x, new_y]

        elif self.level[new_y][new_x] in (self.EMPTY, self.GOAL):
            self.undo_stack.append(copy.deepcopy(self.level))
            if self.level[y][x] == self.GOAL:
                self.level[y][x] = self.GOAL
            else:
                self.level[y][x] = self.EMPTY

            self.player_pos = [new_x, new_y]

        if all(tile != self.BOX for row in self.level for tile in row):
            self.win = True

    def undo_move(self):
        if self.undo_stack:
            self.level = self.undo_stack.pop()

    def reset_game(self, level=2):
        self.level = MapGenerator.generate(level)
        self.player_pos = [1, 1]
        self.undo_stack = []
        self.win = False

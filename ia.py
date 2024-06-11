import math
from collections import deque

class IA:
    def __init__(self, game):
        self.game = game

    def make_move(self):
        x = 0
        player_pos = (self.game.player_x, self.game.player_y)
        box_positions = self.get_box_positions()
        goal_positions = self.get_goal_positions()

        if box_positions and goal_positions:
            target_box, target_goal = self.find_closest_box_goal_pair(box_positions, goal_positions)
            path_to_box = self.bfs(player_pos, target_box)
            if path_to_box:
                next_move = path_to_box[1]
                dx, dy = next_move[0] - player_pos[0], next_move[1] - player_pos[1]
                print (str(dx) + str(dy))
                self.game.moving(dx, dy, self.game.map)
                self.game.signaler_mouvement()

    def get_box_positions(self):
        positions = []
        for y, row in enumerate(self.game.map):
            for x, cell in enumerate(row):
                if cell == 2:
                    positions.append((x, y))
        return positions

    def get_goal_positions(self):
        positions = []
        for y, row in enumerate(self.game.map):
            for x, cell in enumerate(row):
                if cell == 4:
                    positions.append((x, y))
        return positions

    def find_closest_box_goal_pair(self, boxes, goals):
        min_distance = float('inf')
        closest_pair = None
        for box in boxes:
            for goal in goals:
                distance = self.euclidean_distance(box, goal)
                if distance < min_distance:
                    min_distance = distance
                    closest_pair = (box, goal)
        return closest_pair

    def euclidean_distance(self, pos1, pos2):
        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)

    def bfs(self, start, goal):
        queue = deque([start])
        visited = set()
        came_from = {start: None}

        while queue:
            current = queue.popleft()
            if current == goal:
                return self.reconstruct_path(came_from, start, goal)

            for neighbor in self.get_neighbors(current):
                if neighbor not in visited and self.game.map[neighbor[1]][neighbor[0]] != 5:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    came_from[neighbor] = current
        return None

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]
        return neighbors

    def reconstruct_path(self, came_from, start, goal):
        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path
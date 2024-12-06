import pygame
import random

class Maze:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = self.generate_maze(width, height)
        self.player_x, self.player_y = 1, 1  # Starting position

    def generate_maze(self, width, height):
        '''
        creates a maze using a DFS algorithm 
        args: 
            width - the width of the entire maze 
            height - the height of the entire maze
        returns: maze object
        '''
        maze = [[1] * width for _ in range(height)]

        def path(x, y):
            '''
            creates a path throught the maze using random number generation
            args:
                x - the current x position when creating a path
                y - the current y position when creating a path
            returns: none
            '''
            maze[y][x] = 0
            directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
            random.shuffle(directions)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 < nx < width - 1 and 0 < ny < height - 1 and maze[ny][nx] == 1:
                    maze[y + dy // 2][x + dx // 2] = 0
                    path(nx, ny)

        path(1, 1)
        return maze
    
    def draw(self, screen):
        '''
        draws the maze
        args: screen - the pygame surface created in the main loop
        returns: none
        '''
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                color = (255, 255, 255) if cell == 0 else (0, 0, 0)
                pygame.draw.rect(screen, color,  (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
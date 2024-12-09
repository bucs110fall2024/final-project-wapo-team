import pygame 
import random

class Maze:
    def __init__(self):
        self.layout = [[1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 0, 0, 0, 1 ,0, 0, 1],
                     [1, 0, 1, 0, 1, 0, 1, 1],
                     [1, 0, 1, 0, 0, 0, 0, 1],
                     [1, 0, 1, 1, 1, 1, 0, 1],
                     [1, 0, 0, 0, 0, 1, 0, 1],
                     [1, 1, 1, 1, 0, 1, 0, 1],
                     [1, 1, 1, 1, 0, 0, 0, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1],
            ]
        self.TILE_SIZE = 50
        self.exit = (7, 6)
    
    def draw(self, screen):
        for row in range(len(self.layout)):
            for col in range(len(self.layout[row])):
                tile = self.layout[row][col]
                x = col * self.TILE_SIZE
                y = row * self.TILE_SIZE
                if tile == 1:  # Wall
                    pygame.draw.rect(screen, "black", (x, y, self.TILE_SIZE, self.TILE_SIZE))
                elif tile == 0:  # Path
                    pygame.draw.rect(screen, "white", (x, y, self.TILE_SIZE, self.TILE_SIZE))

    def is_path(self, row, col):
        if 0 <= row < len(self.layout) and 0 <= col < len(self.layout[row]):
            return self.layout[row][col] == 0
        return False  # Out of bounds, treat as non-path
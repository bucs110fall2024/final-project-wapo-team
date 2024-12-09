import pygame
from src.maze import Maze
import sys


class Octopus(pygame.sprite.Sprite):
    def __init__(self, maze, img = "assets/octopus.png", score = 0):
        '''
        initializes the player character/Octopus
        args:
            x - initial x coordinate
            y - initial y coordinate
            img - pathway to image
        '''
        super().__init__()

        self.row = 1
        self.col = 1
        self.maze = maze
        
        # self.img = pygame.image.load(img)

    def draw(self, screen):
        x = self.col * self.TILE_SIZE + self.TILE_SIZE // 4
        y = self.row * self.TILE_SIZE + self.TILE_SIZE // 4
        pygame.draw.rect(screen, "blue", (x, y, self.TILE_SIZE // 2, self.TILE_SIZE // 2))

    def move(self, dx, dy):
        new_row = self.row + dy
        new_col = self.col + dx
        if self.maze.is_path(new_row, new_col):  # Check if new position is a path
            self.row = new_row
            self.col = new_col
    def has_reached_exit(self):
        return (self.row, self.col) == self.maze.exit
    
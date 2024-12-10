import pygame 
from src.flower import Flower

class Maze:
    def __init__(self):
        self.layout = [[1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 0, 2, 0, 1, 0, 2, 1],
                      [1, 0, 1, 0, 1, 0, 1, 1],
                      [1, 0, 1, 0, 0, 2, 0, 1],
                      [1, 0, 1, 1, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 1, 0, 1],
                      [1, 1, 0, 1, 0, 1, 0, 1],
                      [1, 2, 0, 1, 0, 0, 2, 1],
                      [1, 1, 1, 1, 1, 1, 5, 1],
                    ]
        self.TILE_SIZE = 50
        self.flowers = []
        for row in range(len(self.layout)):
            for col in range(len(self.layout[row])):
                if self.layout[row][col] == 2:
                    self.flowers.append(Flower(row, col, self.TILE_SIZE))
                    
    def draw(self, screen):
        '''
        draws the maze onto the pygame window
        args:
            screen - the surface that the maze is being drawn onto
        '''
        for row in range(len(self.layout)):
            for col in range(len(self.layout[row])):
                tile = self.layout[row][col]
                x = col * self.TILE_SIZE
                y = row * self.TILE_SIZE
                if tile == 1:  # Wall
                    pygame.draw.rect(screen, "black", (x, y, self.TILE_SIZE, self.TILE_SIZE))
                elif tile == 0:  # Path
                    pygame.draw.rect(screen, "white", (x, y, self.TILE_SIZE, self.TILE_SIZE))
                elif tile == 5:
                    pygame.draw.rect(screen, "green", (x, y, self.TILE_SIZE, self.TILE_SIZE))
                elif tile == 2:
                    pygame.draw.rect(screen, "white", (x, y, self.TILE_SIZE, self.TILE_SIZE))
        
        for flower in self.flowers:
            flower.draw(screen)
        
            
    def is_path(self, row, col):
        '''
        determines if the next row and col are a path or not
        args:
            row - the row that the player is moving onto
            col - the col that the player is moving onto
        returns: 
            the row and col are a path
        '''
        return self.layout[row][col] == 0
    
    def is_exit(self, row, col):
        '''
        determines if the next row and col is the exit or not
        args:
            row - the row that the player is moving onto
            col - the col that the player is moving onto
        returns: 
            the row and col is the exit
        '''
        return self.layout[row][col] == 5
    
    def is_item(self, row, col):
        '''
        determines if the next row and col are a item or not
        args:
            row - the row that the player is moving onto
            col - the col that the player is moving onto
        returns: 
            the row and col is an item
        '''
        return self.layout[row][col] == 2
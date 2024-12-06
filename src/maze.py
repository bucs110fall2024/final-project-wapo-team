import pygame 
import random

class Maze:
    def __init__(self, width, height, tiles):
        self.width = width
        self.height = height
        self.tiles = tiles
        self.colmns = width / tiles
        self.rows = height / tiles
    
    def cell(self, x, y):
        self.x = x 
        self.y = y
        self.walls = {'top':True,
                      'right':True,
                      'bottom':True,
                      'left':True}
        self.visited = False
        pygame.display.flip()
        pygame.time.Clock(30)
    def draw(self):
        x =self.x * TILE            
        y = self.y * TILE 
        if self.visited:
          pygame.draw.rect(self.screen, "black", (x, y, TILE, TILE))
        if self.walls['top']:                
            pygame.draw.line(self.screen, "white", (x, y), (x + TILE, y), 3)
        if self.walls['right']:
            pygame.draw.line(self.screen, "white", (x+ TILE, y), (x + TILE, y + TILE), 3)
        if self.walls['bottom']:
            pygame.draw.line(self.screen, "white", (x +TILE, y + TILE), (x, y + TILE), 3)
        if self.walls['left']:
            pygame.draw.line(self.screen, "white", (x, y + TILE), (x, y), 3)

        self.grid_cells = [Maze.cell(col, row)
                      for row in range(self.rows)
                      for col in range(self.colmns)]
        self.current_cell = self.grid_cells[0]
        self.stack = []
            
    def draw_current_cell(self):
        x = self.x * TILE
        y = self.y * TILE 
        pygame.draw.rect(self.screen, "red", (x+2, y+2, TILE - 2, TILE - 2))
        
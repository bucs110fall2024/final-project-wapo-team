from src.flower import Flower
from src.octopus import Octopus
from src.maze import Maze
import pygame 
import pygame_menu 

class Controller:
  
  def __init__(self, WIDTH = 800, HEIGHT = 600, TILE_SIZE = 50, row = 1, col = 1, state = "START" ):
    #setup pygame data
      self.WIDTH = WIDTH
      self.HEIGHT = HEIGHT
      self.TILE_SIZE = TILE_SIZE
      self.row = row
      self.col = col
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
      self.maze = Maze()
      self.TILE_SIZE = 50
      self.exit = (7, 6)
      
      self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
      pygame.display.set_caption("Escap-o-pus")
      self.state = state 
      
  def mainloop(self):
    #select state loop
      while True:
            if self.state == "START":
                self.menuloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state =="END":
                self.gameoverloop()
  
  
  def menuloop(self):
    
      self.menu = pygame_menu.Menu("Start Screen", self.WIDTH-20, self.HEIGHT/2)
        
      self.menu.add.label("Click anywhere to start the program", max_char=-1, font_size=14)
        
      self.menu.add.button('Start', self.menuloop)
        
      while self.state == "START":
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "GAME"
          self.menu.update(pygame.event.get())
          self.menu.draw(self.screen)
          pygame.display.flip()
            
  def gameloop(self):
      #event loop
      
      while self.state == "GAME":
        maze = Maze()
        Octopus(maze)
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self.state == "END"
          elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    Octopus.move(self, 0, -1)
                elif event.key == pygame.K_DOWN:
                    Octopus.move(self, 0, 1)
                elif event.key == pygame.K_LEFT:
                    Octopus.move(self, -1, 0)
                elif event.key == pygame.K_RIGHT:
                    Octopus.move(self, 1, 0)
          if Octopus.has_reached_exit(self):
              self.state == "END"
          
        
      #redraw
        self.screen.fill("white")
        Maze.draw(self, self.screen)
        Octopus.draw(self, self.screen)
        pygame.display.flip()
        pygame.time.Clock().tick(30)
        
  def gameoverloop(self):
      font_obj = pygame.font.SysFont(None, 48)
      msg = font_obj.render("You win! You may quit any time by closing the program", True, "yellow")
        
      while self.state == "END":
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        
            self.screen.blit(msg, (10, 10))
            pygame.display.flip()
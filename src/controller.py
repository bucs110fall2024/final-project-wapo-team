from src.flower import Flower
from src.octopus import Octopus
from src.maze import Maze
import pygame 
import pygame_menu 

class Controller:
  
  def __init__(self,width = 600, height = 450, tiles = 50, state = "START" ):
    #setup pygame data
      self.width = width
      self.height = height
      self.tiles = tiles
      self.screen = pygame.display.set_mode(self.width, self.height)
      
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
    
      self.menu = pygame_menu.Menu("Start Screen", self.width-20, self.height/2)
        
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
      
      clock = pygame.time.Clock()
      self.screen.fill("blue")
      maze = Maze(self.width, self.height, self.tiles)
      
      while self.state == "GAME":
        for event in pygame.event.get():
          if event.type == pygame.quit():
            self.state == "END"
          
        pygame.display.flip()
        clock.tick(30)
      
      #update data
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
          Octopus.move_up()
        if keys[pygame.K_DOWN]:
          Octopus.move_down()
        if keys[pygame.K_LEFT]:
          Octopus.move_left()
        if keys[pygame.K_RIGHT]:
          Octopus.move_right()
        
      #redraw
        self.screen.fill(0,0,0)
        maze.draw(self.screen)
        pygame.display.flip()
        clock.tick(30)
        
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
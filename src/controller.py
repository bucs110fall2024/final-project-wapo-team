import Flower
import Octopus
import Maze 
import pygame 
import pygame_menu 

class Controller:
  
  def __init__(self):
    #setup pygame data
      pygame.init()
      
      
      
      self.screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE))
      self.width, self.height = pygame.display.get_window_size()
      
      self.state == "START"
      
  def mainloop(self):
    #select state loop
      while True:
            if self.state == "START":
                self.startloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state =="END":
                self.endloop()
  
  
  def menuloop(self):
    
      self.menu = pygame_menu.Menu("Start Screen", self.width-20, self.height/2)
        
      self.menu.add.label("Click anywhere to start the program", max_char=-1, font_size=14)
        
      self.menu.add.button(
            'Start', 
            self.start_game, 
            align=pygame_menu.locals.ALIGN_CENTER
        )
        
      while self.state == "START":
          for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    self.state = "GAME"
          self.menu.update(pygame.event.get())
          self.menu.draw(self.screen)
          pygame.display.flip()
            
  def gameloop(self):
      #event loop
      CELL_SIZE = 20
      WIDTH = 21
      HEIGHT = 21
      clock = pygame.time.Clock()
      maze = Maze(WIDTH, HEIGHT, CELL_SIZE)
      
      while self.state == "GAME":
        for event in pygame.event.get():
          if event.type == pygame.quit():
            self.state == "END"
        
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
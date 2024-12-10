from src.octopus import Octopus
from src.maze import Maze
import pygame 
import pygame_menu 

class Controller:
  
  def __init__(self, WIDTH = 800, HEIGHT = 600, TILE_SIZE = 50, row = 1, col = 1, SCORE = 0 ):
    #setup pygame data
      self.WIDTH = WIDTH
      self.HEIGHT = HEIGHT
      self.TILE_SIZE = TILE_SIZE
      self.row = row
      self.col = col
      
      self.background_img = pygame.image.load("assets/wife.png")
      self.background_img = pygame.transform.scale(self.background_img, (WIDTH, HEIGHT))
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
      self.maze = Maze()
      self.player = Octopus(self.maze)
      
      self.clock = pygame.time.Clock()
      
      
      self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
      pygame.display.set_caption("Escap-o-pus")
      self.state = "START" 
      
  def change_state(self, new_state):
    '''
    changes the game state 
    args:
      new_state - the new game state
    '''
    self.state = new_state
      
  def mainloop(self):
    '''
    selects the game state
    args: None
    '''
    while True:
            if self.state == "START":
                self.menuloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state == "END":
                self.gameoverloop()
  
  
  def menuloop(self):
      '''
      creates the game menu
      args: None
      '''
      self.menu = pygame_menu.Menu("Start Screen", self.WIDTH - 20, self.HEIGHT/2)
      self.menu.add.label("Click anywhere to start the program", max_char=-1, font_size=14)  
      self.menu.add.button('Start', lambda: self.change_state("GAME"))
        
      while self.state == "START":
          self.menu.update(pygame.event.get())
          self.menu.draw(self.screen)
          pygame.display.flip()
            
  def gameloop(self):
      '''
      executes the code during the game, player movement, game quit
      args: None
      '''
      while self.state == "GAME":
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            exit()
          elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.move(0, -1)
                elif event.key == pygame.K_DOWN:
                    self.player.move(0, 1)
                elif event.key == pygame.K_LEFT:
                    self.player.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.move(1, 0)
          if self.maze.is_exit(self.player.row, self.player.col):
            self.change_state("END")
          
          self.screen.fill("white")
          self.maze.draw(self.screen)
          self.player.draw(self.screen)
          self.player.draw_score(self.screen, self.player.SCORE)
          pygame.display.flip()
          self.clock.tick(30)
        
  def gameoverloop(self):
      '''
      executes the code for after the game is won, game win message, background change, high score
      args: None
      '''
      font_obj = pygame.font.SysFont(None, 36)
      msg = font_obj.render("CONGRATULATIONS YOU WON THE GAME", True, "yellow")
      high_score_msg = font_obj.render(f"High Score: {Octopus.high_score}", True, "yellow")
      score_msg = font_obj.render(f"Your score: {self.player.SCORE}", True, "yellow")
      while self.state == "END":
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        self.screen.blit(self.background_img, (0,0))
        self.screen.blit(msg, (10, 10)) 
        self.screen.blit(high_score_msg, (10, 60))
        self.screen.blit(score_msg, (10, 110))
        pygame.display.flip()
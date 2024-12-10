import pygame

class Flower(pygame.sprite.Sprite):
    def __init__(self, row, col, TILE_SIZE, WIDTH = 800, HEIGHT = 600, img = "assets/flower.png"):
        '''
        initializes a flower object
        args: 
            x - starting x coordinate
            y - starting y coordinate
            img_file - path to flower image 
        '''
        super().__init__()
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TILE_SIZE = TILE_SIZE
        self.row = row
        self.col = col
        self.img = img
       
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.image = pygame.image.load(self.img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.TILE_SIZE // 2, self.TILE_SIZE //2))
       
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
        
    def draw(self, screen):
        '''
        draws the flowers onto the screen
        args:
            screen - the surface that the flower is beign drawn onto
        '''
        x = self.col * self.TILE_SIZE + self.TILE_SIZE // 4
        y = self.row * self.TILE_SIZE + self.TILE_SIZE // 4
        screen.blit(self.image, (x, y))
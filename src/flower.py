import pygame

class Flower(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        '''
        initializes a flower object
        args: 
            x - starting x coordinate
            y - starting y coordinate
            img_file - path to flower image 
        '''
        super().__init__()
        self.x = x
        self.y = y
        
        self.image = pygame.image.load(img_file)
        self.image = pygame.transform.scale(self.image, (50, 50))
       
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
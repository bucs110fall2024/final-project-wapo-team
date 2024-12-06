import pygame

class Octopus(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, score = 0):
        '''
        initializes the player character/Octopus
        args:
            x - initial x coordinate
            y - initial y coordinate
            img_file - pathway to image
        '''
        super().__init__()
        
        self.x = x
        self.y = y
        self.score = score
        
        self.image = pygame.image.load(img_file)
        self.image = pygame.transform.scale(self.image, (100, 100))
       
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        
    def move_right(self):
        '''
        moves the player right by one
        args: none
        returns: none
        '''
        self.x += 1 
        
    def move_left(self):
        '''
        mooves the player left by one
        args: none
        returns: none
        '''
        self.x -= 1
        
    def move_up(self):
        '''
        moves the player up by one
        args: none
        returns: none
        '''
        self.y += 1
    def move_down(self):
        '''
        moves the player down by one
        args: none
        returns: none
        '''
        self.y -= 1
    def score_up(self):
        '''
        increases the player score 
        args: none
        returns: player score
        '''
        self.score += 100
        return self.score 

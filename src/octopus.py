import pygame


class Octopus(pygame.sprite.Sprite):
    def __init__(self, maze, row = 1, col = 1, WIDTH = 800, HEIGHT = 600, TILE_SIZE = 50, SCORE = 0, img = "assets/octopus.png", score = 0):
        '''
        initializes the player character/Octopus
        args:
            maze = maze object
            row = initial row postion of the player, default = 1
            col = initial col postion of the player, default = 1
            WIDTH = width of the pygame window
            HEIGHT = height of the pygame window
            TILE_SIZE = tile size for the maze object
            SCORE = player score, starting score is 0
            img - pathway to image
        '''
        super().__init__()

        self.row = row
        self.col = col
        self.maze = maze
        self.TILE_SIZE = TILE_SIZE
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SCORE = SCORE
        self.load_high_score()
        
        self.flowers = []
        
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE // 2, TILE_SIZE //2))
        
    def draw(self, screen):
        '''
        draws the player character/octopus
        args: 
            screen - the surface that the octopus is beign drawn onto
        '''
        x = self.col * self.TILE_SIZE + self.TILE_SIZE // 4
        y = self.row * self.TILE_SIZE + self.TILE_SIZE // 4
        screen.blit(self.image, (x, y))

    def move(self, dx, dy):
        '''
        moves the player character/octopus, if player is moved into a flower tile, the flower gets 
        removed and the player score is increased by 100, then calls update_high_score()
        args:
            dx - change in position of the octopus in the x plane 
            dy - change in position of the octopus in the y plane
        '''
        new_row = self.row + dy
        new_col = self.col + dx
        if self.maze.is_path(new_row, new_col) or self.maze.is_exit(new_row, new_col) or self.maze.is_item(new_row, new_col):  # Check if new position is a path
            self.row = new_row
            self.col = new_col
            
            for flower in self.maze.flowers[:]:
                if flower.row == self.row and flower.col == self.col:
                    self.maze.flowers.remove(flower)
                    self.SCORE += 100
                    self.update_high_score()
                    
    def draw_score(self, screen, SCORE):
        '''
        draws the current player score in the upper left corner
        args:
            screen - the surface that the score is being drawn onto
            SCORE - the current player score
        '''
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {SCORE}", True, "white")
        screen.blit(score_text, (10, 10))
        
    def load_high_score(self):
        '''
        loads the high score from the "highscore.txt" file
        args: None
        '''
        try:
            with open("highscore.txt", "r") as file:
                Octopus.high_score = int(file.read().strip())
        except (FileNotFoundError, ValueError):
            Octopus.high_score = 0 
            
    def save_high_score(self):
        '''
        Saves the high score to the "highscore.txt" file
        args: None
        '''
        with open("highscore.txt", "w") as file:
            file.write(str(Octopus.high_score))

    def update_high_score(self):
        '''
        Updates the high score if the current score is greater
        args: None
        '''
        if self.SCORE > Octopus.high_score:
            Octopus.high_score = self.SCORE
            self.save_high_score()
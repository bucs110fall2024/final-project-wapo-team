import pygame
from src.controller import Controller
from src.octopus import Octopus
from src.flower import Flower
from src.maze import Maze

def main():
    pygame.init()
    game = Controller()
    game.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()

 # -----------------------------------------------------------------
import pygame
import random
import os
# -----------------------------------------------------------------
# S E T T I N G
TITLE = "Mile Millia - The Game"
WIDTH = 2000
HEIGHT = 1000
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# -----------------------------------------------------------------
# set up folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")
# -----------------------------------------------------------------







pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1200,600),0,32)

back = pygame.image.load(os.path.join(img_folder,"Mt.png")).convert()
back = pygame.transform.scale(back,(1200,600))
back2 = pygame.image.load(os.path.join(img_folder,"Mt.png")).convert()
back2= pygame.transform.scale(back2,(1200,600))
x = 0
screenWidth = 600

while True:
    screen.blit(back, (x,0))
    screen.blit(back2,(x-screenWidth,0))
    x = x + 3
    if x == screenWidth:
        x = 0

    msElapsed = clock.tick(100)
    pygame.display.flip()

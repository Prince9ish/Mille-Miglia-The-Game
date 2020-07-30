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
theClock = pygame.time.Clock()

background = pygame.image.load(os.path.join(img_folder,"d.JPG"))
background = pygame.transform.scale(background,(WIDTH,HEIGHT))
background_size = background.get_size()
background_rect = background.get_rect()
screen = pygame.display.set_mode(background_size)
w,h = background_size
x = 0
y = 0

x1 = -w
y1 = 0

running = True

while running:
    screen.blit(background,background_rect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x1 += 50
    x += 50
    screen.blit(background,(x,y))
    screen.blit(background,(x1,y1))
    if x > w:
        x = -w
    if x1 > w:
        x1 = -w
    pygame.display.flip()
    pygame.display.update()
    theClock.tick(1000)

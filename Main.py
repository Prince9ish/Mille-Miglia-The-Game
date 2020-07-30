 # -----------------------------------------------------------------
import pygame
import random
import os
# -----------------------------------------------------------------
# S E T T I N G
TITLE = "Mile Millia - The Game"
WIDTH = 2000
HEIGHT = 1000
FPS = 30

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
# Intiualizes The Game
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
clock = pygame.time.Clock()

# -----------------------------------------------------------------
class Game(pygame.sprite.Sprite):
      def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load(os.path.join(img_folder,"side-7.png")).convert()
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH / 2, HEIGHT /1.5)
            self.speedy = 0

      def update(self) :
            self.speedx = 0
 #           self.acc = vec(0,0)
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE]:
                  self.speedy =- 8
            self.rect.y += self.speedy

# ---------------------------------------------------------------------------------------------------
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


#Load Graphic
background = pygame.image.load(os.path.join(img_folder,"Mt.png")).convert()
background = pygame.transform.scale(background,(WIDTH,HEIGHT))



group = pygame.sprite.Group()
mobs = pygame.sprite.Group()
game = Game()
group.add(game)
for i in range (8):
      m = Mob()
      group.add(m)
      mobs.add(m)


background_size = background.get_size()
background_rect = background.get_rect()
screen = pygame.display.set_mode(background_size)
w,h = background_size


running = True
while running:
      clock.tick(FPS)
      # Process Input
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  running = False

      # Update
      group.update()

      #Check For Collision
      hits = pygame.sprite.spritecollide(game, mobs, False)
      if hits:
            running = False
      # Draw / Render
      screen.blit(background,(0,0))

      group.draw(screen)

      # After
      pygame.display.flip()
pygame.quit()

# M A I N
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - ----- - - - - -- - - - - - - - 
# Import
import pygame as pg
import random
import os
from Setting import*
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  - - - - - - - - ----- - - - - -- - - - - - - -

class Game:
      def __init__(self):
            pg.init()
            pg.mixer.init()
            self.screen = pg.display.set_mode( (WIDTH,HEIGHT) )
            pg.display.set_caption(TITLE)
            self.clock = pg.time.Clock()
            self.running = True

      
      def new(self):
            # Start A New Game
            pass
      
      def run(self):
            # Game Loop
            pass

      def update(self):
            # Update The Game Loop
            pass

      def events(self):
            # Game Loop - Events
            pass

      def draw(self):
            # Game Loop - Draw
            pass
      
      def start_screen(self):
            # S T A R T SCREEN
            pass

      def back_selector(self):
            # S T A R T SCREEN
            pass

      def car_screen(self):
            # S T A R T SCREEN
            pass

      def go_screen(self):
            # GAME OVER SCREEN
            pass
      
g = Game()
g.start_screen()
while g.running:
      g.new()
      g.go_screen()

pg.quit()
      

      

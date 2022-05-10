import pygame as pg
import sys
from settings import *
from debug import debug
from level import Level


class Game:
    def __init__(self):

        # general setup
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption('An isometric adventure')
        self.clock = pg.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()
            pg.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()

import os
import pygame as pg
from random import choice, randrange

class Symbol:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.value = choice(green_katakana)
        self.interval = randrange(5, 30)

    def draw(self, color):
        frames = pg.time.get_ticks()
        if not frames % self.interval:
            self.value = choice(green_katakana if color == 'green' else lightgreen_katakana)
        self.y = self.y + self.speed if self.y < height else - font_size
        screen.blit(self.value, (self.x, self.y))

class Column:
    def __init__(self, x, y):
        self.column_height = randrange(8, 25)
        self.speed = randrange(4, 6)
        self.symbols = [Symbol(x, i, self.speed) for i in range(y, y - font_size * self.column_height, - font_size)]

    def draw(self):
        [symbol.draw('green') if i else symbol.draw('lightgreen') for i, symbol in enumerate(self.symbols)]

os.environ['SDL_VIDEO_CENTERED'] = '1'
width = 800
height = 600
font_size = 20
alpha = 1200

pg.init()
screen = pg.display.set_mode([width, height])
surface = pg.Surface([width, height])
surface.set_alpha(alpha)
clock = pg.time.Clock()

katakana = [chr(int('0x30a0', 16) + i) for i in range(96)]
font = pg.font.Font('font/ms mincho.ttf', font_size)
green_katakana = [font.render(char, True, (0, randrange(30, 256), 0)) for char in katakana]
lightgreen_katakana = [font.render(char, True, pg.Color('lightgreen')) for char in katakana]


symbol_columns = [Column(x, randrange(- height, 0)) for x in range(0, width, font_size)]
while True:
    screen.blit(surface, (0, 0))
    surface.fill(pg.Color('black'))

    [symbol_column.draw() for symbol_column in symbol_columns]

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    pg.display.flip()
    clock.tick(60)
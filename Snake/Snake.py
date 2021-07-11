import pygame
from random import *

pygame.init()

Dist = 600
Size = 30

x, y = randrange(0, Dist, Size), randrange(0, Dist, Size)
Shroom = randrange(0, Dist, Size), randrange(0, Dist, Size)
Mushroom = pygame.image.load('mushroom.png')
buttons = {'w': True, 's': True, 'a': True, 'd': True}
length = 1
snake = [(x, y)]
dx = 0
dy = 0
fps = 10
score = 0

sc = pygame.display.set_mode([Dist, Dist])
clock = pygame.time.Clock()
Score_font = pygame.font.SysFont('Arial', 26, bold = True)
game_over_font = pygame.font.SysFont('Arial', 55, bold = True)

while True:
    sc.fill(pygame.Color('black'))
    [(pygame. draw.rect(sc, pygame.Color('green'), (i, j, Size - 2, Size -2))) for i, j in snake] #Snake
    sc.blit(Mushroom, (*Shroom, Size, Size))
    score_render = Score_font.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(score_render, (5,5))
    x += dx * Size #movement
    y += dy * Size
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == Shroom: #ate shroom
        Shroom = randrange(0, Dist, Size), randrange(0, Dist, Size)
        length += 1
        score += 1
        fps += 1

    if x < 0 or x > Dist - Size or y < 0 or y > Dist - Size or len(snake) != len(set(snake)):
        while True:
            game_over = game_over_font.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(game_over, (Dist // 2 - 140, Dist // 2.5))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and buttons['w']:
        dx, dy = 0, -1
        buttons = {'w': True, 's': False, 'a': True, 'd': True}
    if key[pygame.K_s] and buttons['s']:
        dx, dy = 0, 1
        buttons = {'w': False, 's': True, 'a': True, 'd': True}
    if key[pygame.K_a] and buttons['a']:
        dx, dy = -1, 0
        buttons = {'w': True, 's': True, 'a': True, 'd': False}
    if key[pygame.K_d] and buttons['d']:
        dx, dy = 1, 0
        buttons = {'w': True, 's': True, 'a': False, 'd': True}
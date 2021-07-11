import pygame
from random import *

pygame.init()

width = 640
height = 660
Size = 20
bg = pygame.image.load('space.jpg')
x, y = randrange(100, width - 100, Size), randrange(100, height - 100, Size)
Shroom = randrange(20, width - 20, Size), randrange(40, height - 20, Size)
Mushroom = pygame.image.load('apple.png')
buttons = {'w': True, 's': True, 'a': True, 'd': True}
length = 1
snake = [(x, y)]
dx = 0
dy = 0
fps = 10
score = 0

sc = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
Score_font = pygame.font.SysFont('Arial', 26, bold=True)
game_over_font = pygame.font.SysFont('Arial', 55, bold=True)

while True:
    sc.fill(pygame.Color('black'))
    sc.blit(bg, (20, 40))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, Size - 2, Size - 2))) for i, j in snake]  # Snake
    sc.blit(Mushroom, (*Shroom, Size, Size))
    score_render = Score_font.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(score_render, (5, 5))
    x += dx * Size  # movement
    y += dy * Size
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == Shroom:  # ate shroom
        Shroom = randrange(20, width - 20, Size), randrange(40, height - 20, Size)
        length += 1
        score += 1
        fps += 1

    if x < 20 or x > (width - 20) - Size or y < 40 or y > (height - 20) - Size or len(snake) != len(set(snake)):
        while True:
            game_over = game_over_font.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(game_over, ((width - 20) // 2 - 130, (height - 50) // 2.3))
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
    if key[pygame.K_SPACE]:
        sc.fill(pygame.Color('black'))
        sc.blit(bg, (20, 40))
        x, y = randrange(100, width - 100, Size), randrange(100, height - 100, Size)
        snake = [(x, y)]
        sc.blit(Mushroom, (*Shroom, Size, Size))
        Shroom = randrange(20, width - 20, Size), randrange(40, height - 20, Size)
        score = 0
        length = 1
        dx = 0
        dy = 0


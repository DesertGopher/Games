import pygame
from datetime import datetime
import math

heigth = 600
width = 800
width_half = width / 2
heigth_half = heigth / 2
radius = 250
pygame.init()
screen = pygame.display.set_mode([width, heigth])
clock = pygame.time.Clock()
#bg = pygame.image.load('bg.jpg')
font = pygame.font.SysFont('Verdana', 40)
arrow_radius = {'sec': radius - 10, 'min': radius - 40, 'hour': radius - 70, 'digit': radius - 20}

ARC = radius + 2
clocl_img = pygame.image.load('bg.png').convert_alpha()
bg = pygame.image.load('mist.jpg').convert()
bg_rect = bg.get_rect()
bg_rect.center = width, heigth
dx, dy = 3, 3


minute_arrow = dict(zip(range(60), range(0, 360, 6)))


def arrow_pos(min_arr, sec, rad):
    x = width_half + arrow_radius[rad] * math.cos(math.radians(min_arr[sec]) - math.pi / 2)
    y = heigth_half + arrow_radius[rad] * math.sin(math.radians(min_arr[sec]) - math.pi / 2)
    return x, y


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #screen.fill(pygame.Color('black'))
    #screen.blit(bg, (0, 0))
    dx *= -1 if bg_rect.left > 0 or bg_rect.right < width else 1
    dy *= -1 if bg_rect.top > 0 or bg_rect.bottom < heigth else 1
    bg_rect.centerx += dx
    bg_rect.centery += dy
    screen.blit(bg, bg_rect)
    screen.blit(clocl_img, (0, 0))

    t = datetime.now()
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second

    #pygame.draw.circle(screen, pygame.Color('forestgreen'), (width_half, heigth_half), radius)
    for digit, pos in minute_arrow.items():
        R = 9 if not digit % 3 and not digit % 5 else 6 if not digit % 5 else 2
        pygame.draw.circle(screen, pygame.Color('gainsboro'), arrow_pos(minute_arrow, digit, 'digit'), R, 4)

    pygame.draw.line(screen, pygame.Color('green'), (width_half, heigth_half), arrow_pos(minute_arrow, second, 'sec'), 2)
    pygame.draw.line(screen, pygame.Color('yellow'), (width_half, heigth_half), arrow_pos(minute_arrow, minute, 'min'), 3)
    pygame.draw.line(screen, pygame.Color('red'), (width_half, heigth_half), arrow_pos(minute_arrow, hour, 'hour'), 5)
    pygame.draw.circle(screen, pygame.Color('white'), (width_half, heigth_half), 6)

    time = font.render(f'{t:%H:%M:%S}', True, pygame.Color('green'), pygame.Color('black'))
    screen.blit(time, (20, 20))

    angle = -math.radians(minute_arrow[t.second]) + math.pi / 2
    pygame.draw.arc(screen, pygame.Color('magenta'),
                    (width_half - ARC, heigth_half - ARC, 2 * ARC, 2 * ARC),
                    math.pi / 2, angle, 2)

    pygame.display.flip()
    clock.tick(20)

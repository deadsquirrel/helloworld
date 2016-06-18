#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

# создадим окно (высота, ширина)
window = pygame.display.set_mode((400, 400))

pygame.display.set_caption('ура! это заголовок окна!')

# запишем цвет в RGB
BLUE =  (  0,   0, 255)

#игровой экран
screen = pygame.Surface((400, 400))

# создаем обьект
square = pygame.Surface((40, 40))
# красим обьект , цвета в RGB
square.fill((50, 16, 85))

x = 0
y = 0
square_go_right = True
square_go_down = True

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    # красим окно , цвета в RGB
    screen.fill((50, 16, 85))

    # учим обьект двигаться
    if square_go_right == True:
        x += 1
        if x > 360: # ширина экрана минус ширина обьекта
            square_go_right = False
    else:
        x -= 1
        if x < 0:
            square_go_right = True

    if square_go_down == True:
        y += 2
        if y > 360: # высота экрана минус ширина обьекта
            square_go_down = False
    else:
        y -= 3
        if y < 0:
            square_go_down = True
    
    # указываем что и куда отображаем
       # рисуем-создаем  круг на квадрате
    pygame.draw.circle(square, BLUE, (20, 20), 20, 0)
    screen.blit(square, (x, y))
    window.blit(screen,  (0, 0))
    pygame.display.flip()
    # делаем задержку
    pygame.time.delay(5)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

# создадим окно (высота, ширина)
window = pygame.display.set_mode((400, 400))

pygame.display.set_caption('ура! это заголовок окна!')

#игровой экран
screen = pygame.Surface((400, 400))

# создаем обьект
square = pygame.Surface((40, 40))
square.fill((0, 255, 0))


done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame. QUIT:
            done = False


    #красим окно , цвета в RGB
    screen.fill((50, 16, 85))

    # указываем что и куда отображаем
    screen.blit(square, (0, 0))
    window.blit(screen,  (0, 0))
    pygame.display.flip()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

# создадим окно (высота, ширина)
window = pygame.display.set_mode((400, 400))

pygame.display.set_caption('ура! это заголовок окна!')

#игровой экран
screen = pygame.Surface((400, 400))

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame. QUIT:
            done = False


    #красим окно , цвета в RGB
    screen.fill((50, 16, 85))
    
    window.blit(screen,  (0, 0))
    pygame.display.flip()

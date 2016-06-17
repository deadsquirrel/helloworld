#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

# создадим окно (высота, ширина)
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Game!')

#игровой экран
screen = pygame.Surface((400, 400))

#вводим класс для героя
class Sprite:
    def __init__ (self,xpos,ypos,filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=pygame.image.load(filename)
# фон делаем прозрачным
        self.bitmap.set_colorkey((255,255,255))
# отображаем обьект на игровой экран
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))

# создаем героев
boy1 = Sprite(0,0, 'face1.png')
boy2 = Sprite(40,40, 'face2.png')
        

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame. QUIT:
            done = False

    # красим окно , цвета в RGB
    screen.fill((50, 16, 85))

# отобразим обьекты
    boy1.render()
    boy2.render()

    window.blit(screen,  (0, 0))
    pygame.display.flip()
    # делаем задержку
    pygame.time.delay(5)

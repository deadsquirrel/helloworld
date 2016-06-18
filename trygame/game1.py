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
        screen.blit(self.bitmap,(self.x, self.y))

# создаем героев
boy1 = Sprite(0,0, 'face1.png')
# новый атрибут герою - рычаг управления_1
boy1_go_right = True
boy1_go_down = True

boy2 = Sprite(40,40, 'face2.png')
# новый атрибут герою - рычаг управления_2
boy2_go_right = True
boy2_go_down = True

done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

# красим окно , цвета в RGB
    screen.fill((50, 16, 85))

# учим обьекты двигаться
# boy1
    if boy1_go_right == True:
        boy1.x += 1
        if boy1.x > 360: # ширина экрана минус ширина обьекта
            boy1_go_right = False
    else:
        boy1.x -= 1
        if boy1.x < 0:
            boy1_go_right = True

    if boy1_go_down == True:
        boy1.y += 1
        if boy1.y > 360: # высота экрана минус ширина обьекта
            boy1_go_down = False
    else:
        boy1.y -= 1
        if boy1.y < 0:
            boy1_go_down = True

    # boy2
    
    if boy2_go_right == True:
        boy2.x += 1
        if boy2.x > 360: # ширина экрана минус ширина обьекта
            boy2_go_right = False
    else:
        boy2.x -= 3
        if boy2.x < 0:
            boy2_go_right = True

    if boy2_go_down == True:
        boy2.y += 1
        if boy2.y > 360: # высота экрана минус ширина обьекта
            boy2_go_down = False
    else:
        boy2.y -= 2
        if boy2.y < 0:
            boy2_go_down = True
    
            
    # отобразим обьекты
    boy1.render()
    boy2.render()

    window.blit(screen,  (0, 0))
    pygame.display.flip()
    # делаем задержку
    pygame.time.delay(15)

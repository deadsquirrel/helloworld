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
leo = Sprite(200,0, 'face1.png')
# новый атрибут герою - рычаг управления_1
leo_go_right = True
leo_go = True

ian = Sprite(200,360, 'face2.png')
# новый атрибут герою - рычаг управления_2
ian_go_right = True
ian_go = True


# функция проверки пересечения объектов. 40 - величина ширины объектов
def Intersect(x1, x2, y1, y2):
    if ((x1 > x2-40) and (x1 < x2+40) and (y1 > y2-40) and (y1 < y2+40)) :
        return 1
    else:
        return 0
                
done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
           
# красим окно , цвета в RGB
    screen.fill((5, 6, 5))
    
    if leo_go == True:
        leo.y += 1
        if leo.y > 360: 
            leo_go = False
    else:
        leo.y -= 1
        if leo.y < 0:
            leo_go = True

    if ian_go == True:
        ian.y -= 1
        if ian.y < 0: 
            ian_go = False
    else:
        ian.y += 1
        if ian.y > 360:
            ian_go = True


    if Intersect (leo.x, ian.x, leo.y, ian.y) == 1:
        if leo_go == True:
            leo_go = False
        else:
            leo_go = True
        if ian_go == True:
            ian_go = False
        else:
            ian_go = True
   
# отобразим обьекты
    leo.render()
    ian.render()

    window.blit(screen,  (0, 0))
    pygame.display.flip()
    # делаем задержку
    pygame.time.delay(15)

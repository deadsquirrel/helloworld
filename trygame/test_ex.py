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
        self.bitmap.set_colorkey((0,0,0))
# отображаем обьект на игровой экран
    def render(self):
        screen.blit(self.bitmap,(self.x, self.y))

# создаем героев
zet = Sprite(200,0, 'apple.jpeg')
# новый атрибут герою - рычаг управления_1
zet_go_right = True
zet_go = True

hero= Sprite(200,360, 'luchnik.jpg')
# новый атрибут герою - рычаг управления_2
hero_go_right = True
hero_go = True

strela= Sprite(220,360, 'strela.png')

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
    screen.fill((255, 255, 8))
    

    '''
    if Intersect (zet.x, hero.x, zet.y, hero.y) == 1:
        if zet_go == True:
            zet_go = False
        else:
            zet_go = True
        if hero_go == True:
            hero_go = False
        else:
            hero_go = True
    '''   
# отобразим обьекты
    zet.render()
    hero.render()
    strela.render()
    
    window.blit(screen,  (0, 0))
    pygame.display.flip()
    # делаем задержку
    pygame.time.delay(15)

'''
    
    if zet_go == True:
        zet.y += 1
        if zet.y > 360: 
            zet_go = False
    else:
        zet.y -= 1
        if zet.y < 0:
            zet_go = True

    if hero_go == True:
        hero.y -= 1
        if hero.y < 0: 
            hero_go = False
    else:
        hero.y += 1
        if hero.y > 360:
            hero_go = True


    if Intersect (zet.x, hero.x, zet.y, hero.y) == 1:
        if zet_go == True:
            zet_go = False
        else:
            zet_go = True
        if hero_go == True:
            hero_go = False
        else:
            hero_go = True
   '''

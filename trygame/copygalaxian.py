#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random

# создадим окно (высота, ширина)
SCREEN_WIDTH = 800
SCREEN_HIGHT = 700

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption('Galaxian')

#игровой экран
screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HIGHT))

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

# создаем самолетик
plane = Sprite(SCREEN_WIDTH/2, SCREEN_HIGHT-60, 'pl.png')
# новый атрибут герою - рычаг управления_1
pl_go_right = True

# создаем муху
x_b = random.randint(100, SCREEN_WIDTH-100)
y_b = random.randint(0, SCREEN_HIGHT/2)
fly = Sprite(x_b,y_b, 'f1.png')
# новый атрибут герою - рычаг управления_2
#fly_go_right = True
rl = random.randint(0,1)
if rl == 0:
    fly_go_r = True
else:
    fly_go_r = False
ud = random.randint(0,1)
if ud == 0:
    fly_go_d = True
else:
    fly_go_d = False


#  скорость. подумаем позже, нужна ли она
rr = random.uniform(1,2)
print rr
speedb = 1*rr
rrr = random.uniform(2,3)
speedp = 1*rrr


# вводим переменную для счета
score1 = 0



# функция проверки пересечения объектов. db - величина ширины объектов

def Intersect(x1, x2, y1, y2, db1, db2):
    if (x2>x1 and (x2+db2) <= (x1+db1)) and y2 <= (y1+db1):
        return 1
    else:
        return 0             
    
done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
           
# красим окно , цвета в RGB
    screen.fill((115, 106, 200))
    # событие - нажатие клавиш
    if e.type == pygame.KEYDOWN:
        # перемещение героя
        if e.key == pygame.K_a:
            if plane.x > 0:
                plane.x -= speedp
        if e.key == pygame.K_d:
            if plane.x < (SCREEN_WIDTH-60):
                plane.x += speedp



            
                
#    if Intersect (plane.x, fly.x, plane.y, fly.y, plane.width, fly.width) == 1:
#        print 'BABAX!'
        '''
        if fly_go_r == True and fly_go_d == False:
            fly_go_r = True
            fly_go_d = True
        if fly_go_r == False and fly_go_d == False:
            fly_go_r = False
            fle_go_d = True
        '''     

            
# отобразим обьекты
    plane.render()
    fly.render()
   
    window.blit(screen,  (0, 0))
    pygame.display.flip()
    # делаем задержку
    pygame.time.delay(15)

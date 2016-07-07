#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random

# создадим окно (высота, ширина)
SCREEN_WIDTH = 500
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_caption('Game!')

#игровой экран
screen = pygame.Surface((SCREEN_WIDTH, SCREEN_WIDTH))

#вводим класс для героя
class Sprite:
    def __init__ (self,xpos,ypos,filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=pygame.image.load(filename)
# фон делаем прозрачным
        self.bitmap.set_colorkey((255,25,255))
# отображаем обьект на игровой экран
    def render(self):
        screen.blit(self.bitmap,(self.x, self.y))

# создаем героев
leo = Sprite(SCREEN_WIDTH/2,0, 'face1.png')
# новый атрибут герою - рычаг управления_1
leo_go_right = True
leo_go = True

ian = Sprite(SCREEN_WIDTH/2,(SCREEN_WIDTH-40), 'face2.png')
# новый атрибут герою - рычаг управления_2
ian_go_right = True
ian_go = True

x_b = random.randint(0, SCREEN_WIDTH)
y_b = random.randint(0, SCREEN_WIDTH)
ball = Sprite(x_b,y_b, 'bb1.png')
rl = random.randint(0,1)
if rl == 0:
    ball_go_r = True
else:
    ball_go_r = False
ud = random.randint(0,1)
if ud == 0:
    ball_go_d = True
else:
    ball_go_d = False


# придумаем скорость
rr = random.uniform(1,2)
print rr
speedb = 1*rr
rrr = random.uniform(2,3)
speedl = 1*rrr
speedi = 1*rrr

# уменьшаем время отклика клавиатуры (проверить)
pygame.key.set_repeat(1,1)


# функция проверки пересечения объектов. 40 - величина ширины объектов

def Intersect(x1, x2, y1, y2, db1, db2):
    if (x2>x1 and (x2+db2) < (x1+db1)) and y2 <= (y1+db1):
        return 1
    else:
        return 0             

def Intersect2(x1, x2, y1, y2, db1, db2):
    if (x2>x1 and (x2+db2) < (x1+db1)) and y1 <= y2+db2:
        return 1
    else:
        return 0             

    
done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
           
# красим окно , цвета в RGB
    screen.fill((15, 106, 15))
    # событие - нажатие клавиш
    if e.type == pygame.KEYDOWN:
        # перемещение героя
        if e.key == pygame.K_a:
            if leo.x > 0:
                leo.x -= speedl
        if e.key == pygame.K_d:
            if leo.x < (SCREEN_WIDTH-40):
                leo.x += speedl
        if e.key == pygame.K_w:
            if leo.y > 0:
                leo.y -= speedl
        if e.key == pygame.K_s:
            if leo.y < (SCREEN_WIDTH/2-40):
                leo.y += speedl

        # перемещение героя 2
        if e.key == pygame.K_LEFT:
            if ian.x > 0:
                ian.x -= speedi
        if e.key == pygame.K_RIGHT:
            if ian.x < (SCREEN_WIDTH-40):
                ian.x += speedi
        if e.key == pygame.K_UP:
            if ian.y > (SCREEN_WIDTH/2):
                ian.y -= speedi
        if e.key == pygame.K_DOWN:
            if ian.y < (SCREEN_WIDTH-40):
                ian.y += speedi

# движение мяча   
    if ball_go_r == True:
        ball.x += speedb
        if ball.x > (SCREEN_WIDTH - 15 - speedb): 
            ball_go_r = False
    else:
        ball.x -= speedb
        if ball.x < 0:
            ball_go_r = True

    if ball_go_d == True:
        ball.y += speedb
        if ball.y > (SCREEN_WIDTH - 15 - speedb): 
            ball_go_d = False
    else:
        ball.y -= speedb
        if ball.y < 0:
            ball_go_d = True

            
                
    if Intersect (leo.x, ball.x, leo.y, ball.y, 40, 15) == 1:
        if ball_go_r == True and ball_go_d == False:
            print '1'
            ball_go_r = True
            ball_go_d = True
        if ball_go_r == False and ball_go_d == False:
            print '2'
            ball_go_r = False
            ball_go_d = True
     
    if Intersect2 (ian.x, ball.x, ian.y, ball.y, 40, 15) == 1:
        #    if Intersect (ball.x, ian.x, ball.y, ian.y, 15, 40) == 1:
        if ball_go_r == True and ball_go_d == True:
            print '3'
            ball_go_r = True
            ball_go_d = False
        if ball_go_r == False and ball_go_d == True:
            print '4'
            ball_go_r = False
            ball_go_d = False

            
# отобразим обьекты
    leo.render()
    ian.render()
    ball.render()

    
    window.blit(screen,  (0, 0))
    pygame.display.flip()
    # делаем задержку
    pygame.time.delay(15)

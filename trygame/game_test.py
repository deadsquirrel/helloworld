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

ball = Sprite(200,200, 'bb1.png')
ball_go = True

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
    screen.fill((15, 106, 15))
    '''  
    if leo_go == True:
        leo.y += 1
        if leo.y > 360: 
            leo_go = False
    else:
        leo.y -= 1
        if leo.y < 0:
            leo_go = True
    '''
    # событие - нажатие клавиш
    if e.type == pygame.KEYDOWN:
        # перемещение героя
        if e.key == pygame.K_a:
            if leo.x > 0:
                leo.x -= 1
        if e.key == pygame.K_d:
            if leo.x < 360:
                leo.x += 1
        if e.key == pygame.K_w:
            if leo.y > 0:
                leo.y -= 1
        if e.key == pygame.K_s:
            if leo.y < 360:
                leo.y += 1

        # перемещение героя 2
        if e.key == pygame.K_LEFT:
            if ian.x > 0:
                ian.x -= 1
        if e.key == pygame.K_RIGHT:
            if ian.x < 360:
                ian.x += 1
        if e.key == pygame.K_UP:
            if ian.y > 0:
                ian.y -= 1
        if e.key == pygame.K_DOWN:
            if ian.y < 360:
                ian.y += 1

                '''
    if ian_go == True:
        ian.y -= 1
        if ian.y < 0: 
            ian_go = False
    else:
        ian.y += 1
        if ian.y > 360:
            ian_go = True
               '''

    if ball_go == True:
        ball.x += 3
        if ball.x > 385: 
            ball_go = False
    else:
        ball.x -= 3
        if ball.x < 0:
            ball_go = True

    if ball_go == True:
        ball.y += 2
        if ball.y > 385: 
            ball_go = False
    else:
        ball.y -= 2
        if ball.y < 0:
            ball_go = True
            
                
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
    ball.render()

    
    window.blit(screen,  (0, 0))
    pygame.display.flip()
    # делаем задержку
    pygame.time.delay(15)

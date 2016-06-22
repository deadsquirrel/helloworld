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
zet.step = 1

hero= Sprite(200,360, 'luchnik.jpg')
# новый атрибут герою - рычаг управления_2
hero_go_right = True
hero_go = True

strela = Sprite(-10,350, 'strela.png')
strela_go = False

# функция проверки пересечения объектов. 40 - величина ширины объектов
def Intersect(x1, x2, y1, y2, db1, db2):
    if ((x1 > x2-db1) and (x1 < x2+db2) and (y1 > y2-db1) and (y1 < y2+db2)) :
        return 1
    else:
        return 0
                
done = True
# дублируем клавишу, пока оно нажата pygame.key.set_repeat (a, b)
# a - задержка перед первым дублированием, мс;  b - задержка между остальными дублированиями
pygame.key.set_repeat (1, 1)

while done:
    # обработчик событий
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
           
    # красим окно , цвета в RGB
    screen.fill((255, 255, 8))

    # движение цели
    if zet_go == True:
        zet.x += zet.step
        if zet.x > 360: 
            zet_go = False
    else:
        zet.x -= zet.step
        if zet.x < 0:
            zet_go = True

    # событие - нажатие клавиш
    if e.type == pygame.KEYDOWN:
        # перемещение героя
        if e.key == pygame.K_LEFT:
            if hero.x > 10:
                hero.x -= 1
        if e.key == pygame.K_RIGHT:
            if hero.x < 350:
                hero.x += 1
        if e.key == pygame.K_UP:
            if hero.y > 70:
                hero.y -= 1
        if e.key == pygame.K_DOWN:
            if hero.y < 350:
                hero.y += 1
        # запуск стрелы
        if e.key == pygame.K_SPACE:
            if strela_go == False:
                strela.x = hero.x + 15
                strela.y = hero.y - 15
                strela_go = True
        # событие - движение мыши
        if e.type == pygame.MOUSEMOTION:
            pygame.mouse.set_visible(True)
            m = pygame.mouse.get_pos()
            print m
            # pygame.mouse.get_pos()
            # (x, y)
            hero.x = m[0]
            hero.y = m[1]
        # событие - нажатие кнопки мыши
        # mousebuttondown
        # left - 1, right - 2, center - 3
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if strela_go == False:
                    strela.x = hero.x+15
                    strela.y = hero.y
                    strela_go = True
    # перемещение стрелы
    if strela.y < 0:
        strela_go = False
        
    if strela_go == False:
        strela.y = 350
        strela.x = -10
    else:
        strela.y -= 1
  

    # столкновение стрелы и цели
    if Intersect (strela.x, zet.x, strela.y, zet.y, 10, 40) == 1:
        strela_go = False
        print ("Yes!")
        zet.step += 0.2
          
# отобразим обьекты
    strela.render()
    zet.render()
    hero.render()
        
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

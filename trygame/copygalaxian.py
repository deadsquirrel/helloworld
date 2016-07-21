#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random

# создадим окно (высота, ширина)
SCREEN_WIDTH = 800
SCREEN_HIGHT = 700

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption('Galaxian')

timer = pygame.time.Clock()


#игровой экран
screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HIGHT))

#вводим класс для героя
# надо переписать класс sprite c учетом
#
#  File "copygalaxian.py", line 123, in <module>
#  flies_hit_list = pygame.sprite.spritecollide(bom, fly_list, True)  
#  File "/usr/lib/python2.7/dist-packages/pygame/sprite.py", line 1337,
#  in spritecollide
#  spritecollide = sprite.rect.colliderect

class Sprite:
    def __init__ (self,xpos,ypos,width,hight,filename):
        self.x=xpos
        self.y=ypos
        self.w=width
        self.h=hight
        self.bitmap=pygame.image.load(filename)
# фон делаем прозрачным
        self.bitmap.set_colorkey((255,255,255))
# отображаем обьект на игровой экран
    def render(self):
        screen.blit(self.bitmap,(self.x, self.y))

# Это список спрайтов. Каждый мух добавляется в этот список.
# Список управляется классом, называющимся 'Group.'
# этот список не содержит игрока и пулю
fly_list = pygame.sprite.Group()
 
# Это список каждого спрайта. Все блоки, а также блок игрока.
all_sprites_list = pygame.sprite.Group()
        
# создаем самолетик
plane = Sprite(SCREEN_WIDTH/2, SCREEN_HIGHT-60, 60,0, 'pl.png')
all_sprites_list.add_internal(plane)
# новый атрибут герою - рычаг управления_1
pl_go_right = True

# создаем строй мух
# координаты первой как точка отсчета - скорее всего уже не нужна

for i in range(50):
    # ее местоположение
    x_f = random.randint(100, SCREEN_WIDTH/8)
    y_f = random.randint(50, SCREEN_HIGHT/2)
    # создадем муху
    fly = Sprite(x_f,y_f, 50, 37, 'f1.png')
    # муху в строй
    fly_list.add_internal(fly)
    all_sprites_list.add_internal(fly)
    
'''
остальных мух пока не создаем
x_f2 = random.randint(x_f+100, x_f+SCREEN_WIDTH/8)
fly2 = Sprite(x_f2,y_f, 50, 37, 'f1.png')

x_f3 = random.randint(x_f2+100, x_f2+SCREEN_WIDTH/8)
fly3 = Sprite(x_f3,y_f, 50, 37, 'f1.png')
'''


boom1 = Sprite(-200,-200, 140, 110, 'boom1.png')
boom2 = Sprite(-200,-200, 140, 110, 'boom2.png')
boom3 = Sprite(-200,-200, 140, 110, 'boom3.png')
boom = Sprite(-200,-200, 140, 110, 'boom.png')


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

bom = Sprite(-10, SCREEN_HIGHT, 10, 0, 'bom.png')
bom_go = False
all_sprites_list.add_internal(bom)

    
#  скорость. 
rr = random.uniform(1,2)
print rr
speedb = 1*rr+1

speedf = 0.5
rrr = random.uniform(2,3)
speedp = 1*rrr


# вводим переменную для счета
score = 0



# функция проверки пересечения объектов. db - величина ширины объектов
#dy-высота объекта
'''
def Intersect(x1, x2, y1, y2, db1, db2, dy1):
    if (x2>=x1 and (x2+db2) <= (x1+db1)) and y2 <= (y1+dy1):
        return 1
    else:
        return 0             
'''
# Проверим иначе на столкновение
# проверяем спрайт бомбы на столкновение с мухоми
flies_hit_list = pygame.sprite.spritecollide(bom, fly_list, True)  

# Проверить список столкновений.
if len(flies_hit_list) > 0:
    score +=len(flies_hit_list)
    print( score )


    
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
        if e.key == pygame.K_LEFT:
            if plane.x > 0:
                plane.x -= speedp
        if e.key == pygame.K_RIGHT:
            if plane.x < (SCREEN_WIDTH-60):
                plane.x += speedp

        # стреляем
        if e.key == pygame.K_SPACE:
            if bom_go == False:
                bom.x = plane.x + 25
                bom.y = plane.y 
                bom_go = True

    # перемещение пули
    if bom.y < 0:
        bom_go = False
        
    if bom_go == False:
        bom.y = SCREEN_HIGHT
        bom.x = -10
    else:
        bom.y -= speedb+2

    # fly flying
    if fly_go_r == True:
        fly.x += speedf
        if fly.x > (x_f+100): 
            fly_go_r = False
    else:
        fly.x -= speedf
        if fly.x < 0:
            fly_go_r = True
    '''
    # fly2 flying никто никуда не летит
    if fly_go_r == True:
        fly2.x += speedf
        if fly2.x > (x_f2+100): 
            fly_go_r = False
    else:
        fly2.x -= speedf
        if fly2.x < x_f:
            fly_go_r = True

    # fly3 flying
    if fly_go_r == True:
        fly3.x += speedf
        if fly3.x > (x_f3+100): 
            fly_go_r = False
    else:
        fly3.x -= speedf
        if fly3.x < x_f2:
            fly_go_r = True
    '''
    '''
    if fly_go_d == True:
        fly.y += speedf
        if fly.y > (SCREEN_WIDTH/2 - speedf): 
            fly_go_d = False
    else:
        fly.y -= speedf
        if fly.y < 0:
            fly_go_d = True
     '''

    if Intersect (fly.x, bom.x, fly.y, bom.y, fly.w, bom.w, fly.h) == 1:
        bom_go = False
        print 'BABAX!'
        boom1.x = fly.x-45
        boom1.y = fly.y-37
        fly.x = -50
        fly.y = -50
        '''фигня
        меняем вместе с итерацие
        timer.tick(160)
        print 'BABAX1!'
        boom2.x = boom1.x
        boom2.y = boom1.y
        timer.tick(160)
        print 'BABAX2!'
        boom3.x = boom2.x
        boom3.y = boom2.y
        timer.tick(160)
        print 'BABAX3!'
        boom.x = boom3.x
        boom.y = boom3.y

        #        pygame.time.delay(13)

        '''
        
    '''
        if fly_go_r == True and fly_go_d == False:
            fly_go_r = True
            fly_go_d = True
        if fly_go_r == False and fly_go_d == False:
            fly_go_r = False
            fly_go_d = True
    '''     

            
    # отобразим обьекты
    boom1.render()
    boom2.render()
    boom3.render()
    boom.render()
    bom.render()
    plane.render()
    fly.render()
#    fly2.render()
#    fly3.render()
    boom1.render()
    boom2.render()
    boom3.render()
    boom.render()
   
    window.blit(screen,  (0, 0))
    pygame.display.flip()
    # делаем задержку
    pygame.time.delay(15)

import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.mixer.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
purple = (255,0,255)

setDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Road Crosser')

FPS = 30
fpsTime = pygame.time.Clock()

game_sound = pygame.mixer.Sound("busy_road.ogg")
end_sound = pygame.mixer.Sound("end_sound.ogg")
pygame.mixer.music.set_volume(0.4)

car1 = pygame.image.load("car.png")
car2 = pygame.image.load("car3.png")
car3 = pygame.image.load("car2.png")
truck = pygame.image.load("truck.png")

c6x = 0
c5x = 0
c5x = 0
c4x = 0
c3x = 0
c2x = 0
c1x = 0

c1y = 0
c2y = 100
c3y = 200
c4y = 300
c5y = 400
c6y = 500

speed_list = []
for i in range(6):
    import random
    r = random.randint(5,30)
    speed_list.append(r)

backround3 = pygame.image.load("backround2.jpg")
pause = pygame.image.load("pausemenu.jpg")
start = pygame.image.load("startmenu.jpg")
end = pygame.image.load("gameover.jpg")

chicken2 = pygame.image.load("chicken2.png")
chickenY = 550
chickenX = 250

def car_spawn1():
    setDisplay.blit(truck,(c6x,c1y))
    setDisplay.blit(car1,(c5x,c2y))
    setDisplay.blit(car2,(c4x,c3y))
    setDisplay.blit(car3,(c3x,c4y))
    setDisplay.blit(truck,(c2x,c5y))
    setDisplay.blit(car1,(c1x,c6y))

def car_spawn2():
    setDisplay.blit(car1,(c1x,c1y))
    setDisplay.blit(car3,(c2x,c2y))
    setDisplay.blit(car2,(c3x,c3y))
    setDisplay.blit(truck,(c4x,c4y))
    setDisplay.blit(car1,(c5x,c5y))
    setDisplay.blit(car3,(c6x,c6y))

def car_spawn3():
    setDisplay.blit(car2,(c6x,c1y))
    setDisplay.blit(car3,(c5x,c2y))
    setDisplay.blit(car1,(c4x,c3y))
    setDisplay.blit(truck,(c3x,c4y))
    setDisplay.blit(car3,(c2x,c5y))
    setDisplay.blit(truck,(c1x,c6y))


chicken_status = "moving"
c = 0
s = 0
q = 1
p = 0
ch = 0
while True:
    if q == 0:
        if p == 0:
            game_sound.play(-1)
            p = p+1
        if c%3 == 0 or c == 0:
            if c == 0:
                backround3 = pygame.image.load("backround.jpg")
            elif c%3 == 0:
                backround3 = pygame.image.load("backround2.jpg")
                
            setDisplay.blit(backround3,(0,0))
            car_spawn1()

            if chickenX < c1x + 100 and chickenX > c1x:
                if chickenY == c6y:
                    q = 2
                    
            if chickenX < c2x + 100 and chickenX > c2x:
                if chickenY == c5y:
                    q = 2

            if chickenX < c3x + 100 and chickenX > c3x:
                if chickenY == c4y:
                    q = 2

            if chickenX < c4x + 100 and chickenX > c4x:
                if chickenY == c3y:
                    q = 2

            if chickenX < c5x + 100 and chickenX > c5x:
                if chickenY == c2y:
                    q = 2

            if chickenX < c6x + 100 and chickenX > c6x:
                if chickenY == c1y:
                    q = 2

        elif c%3 == 1:
            setDisplay.blit(backround3,(0,0))
            car_spawn2()

            if chickenX < c1x + 100 and chickenX > c1x:
                if chickenY == c1y:
                    q = 2
                
            if chickenX < c2x + 100 and chickenX > c2x:
                if chickenY == c2y:
                    q = 2
                
            if chickenX < c3x + 100 and chickenX > c3x:
                if chickenY == c3y:
                    q = 2
                
            if chickenX < c4x + 100 and chickenX > c4x:
                if chickenY == c4y:
                    q = 2
                
            if chickenX < c5x + 100 and chickenX > c5x:
                if chickenY == c5y:
                    q = 2
                
            if chickenX < c6x + 100 and chickenX > c6x:
                if chickenY == c6y:
                    q = 2

        elif c%3 == 2:
            setDisplay.blit(backround3,(0,0))
            car_spawn3()

            if chickenX < c1x + 100 and chickenX > c1x:
                if chickenY == c6y:
                    q = 2
                    
            if chickenX < c2x + 100 and chickenX > c2x:
                if chickenY == c5y:
                    q = 2

            if chickenX < c3x + 100 and chickenX > c3x:
                if chickenY == c4y:
                    q = 2

            if chickenX < c4x + 100 and chickenX > c4x:
                if chickenY == c3y:
                    q = 2

            if chickenX < c5x + 100 and chickenX > c5x:
                if chickenY == c2y:
                    q = 2

            if chickenX < c6x + 100 and chickenX > c6x:
                if chickenY == c1y:
                    q = 2            
        
        if chicken_status == "moving":            
            n = speed_list[0]
            c1x = c1x + n
            if c1x >= 800:
                c1x = c1x - 800

            n = speed_list[1]
            c2x = c2x + n
            if c2x >= 800:
                c2x = c2x - 800

            n = speed_list[2]
            c3x = c3x + n
            if c3x >= 800:
                c3x = c3x - 800

            n = speed_list[3]
            c4x = c4x + n
            if c4x >= 800:
                c4x = c4x - 800

            n = speed_list[4]
            c5x = c5x + n
            if c5x >= 800:
                c5x = c5x - 800

            n = speed_list[5]
            c6x = c6x + n
            if c6x >= 800:
                c6x = c6x - 800
            
        if chickenY < 20:
            chickenY = 550
            chickenX = 300
            c = c + 1   
          
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if (event.key == K_LEFT):
                   chickenX = chickenX - 50
                   if chickenX <= -50:
                       chickenX = chickenX + 50

                elif (event.key == K_RIGHT):
                   chickenX = chickenX + 50
                   if chickenX >= 750:
                       chickenX = chickenX - 50

                elif (event.key == K_UP):
                   chickenY = chickenY - 50
                   if chickenY <= -50:
                       chickenY = chickenY + 50

                elif (event.key == K_DOWN):
                    chickenY = chickenY + 50
                    if chickenY >= 750:
                       chickenY = chickenY -50

                if (event.key == K_ESCAPE):
                    q = 3
        
        setDisplay.blit(chicken2,(chickenX,chickenY))
        font = pygame.font.SysFont("arial", 50)
        text = font.render("Score: " + str(c), True, white)
        setDisplay.blit(text,(500,50))
        

    elif q == 1:
        setDisplay.blit(start,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == K_SPACE):
                    q = 0
                
                if (event.key == K_c):
                    ch = ch+1
                 
        if ch%3 == 2:
            chicken2 = pygame.image.load("dog.jpg")
            start = pygame.image.load("startmenu_dog.jpg")
            setDisplay.blit(start,(0,0))
        elif ch%3 == 0:
            chicken2 = pygame.image.load("chicken2.png")
            start = pygame.image.load("startmenu.jpg")
            setDisplay.blit(start,(0,0))
        elif ch%3 == 1:
            chicken2 = pygame.image.load("cat.jpg")
            start = pygame.image.load("startmenu_cat.jpg")
            setDisplay.blit(start,(0,0))

        font2 = pygame.font.SysFont("aria",20)
        text2 = font2.render("Press C to change character", True, white)
        setDisplay.blit(text2,(0,0))


    elif q == 2:
        for i in range(999):
            if s == 0:
                game_sound.stop()
                end_sound.play()
                s = s+1
                print("Score:",c)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == K_SPACE):
                    q = 0
                    s = 0
                    c = 0
                    p = 0
                    chickenX = 400
                    chickenY = 550

                elif (event.key == K_c):
                    ch = ch+1

        if ch%3 == 2:
            chicken2 = pygame.image.load("dog.jpg")
            end = pygame.image.load("gameover_dog.jpg")
            setDisplay.blit(end,(0,0))
        elif ch%3 == 0:
            chicken2 = pygame.image.load("chicken2.png")
            end = pygame.image.load("gameover.jpg")
            setDisplay.blit(end,(0,0))
        elif ch%3 == 1:
            chicken2 = pygame.image.load("cat.jpg")
            end = pygame.image.load("gameover_cat.jpg")
            setDisplay.blit(end,(0,0))

        setDisplay.blit(end,(0,0))
        font = pygame.font.SysFont("arial", 50)
        text = font.render("Score: " + str(c), True, white)
        font2 = pygame.font.SysFont("aria",20)
        text2 = font2.render("Press C to change character", True, white)
        setDisplay.blit(text2,(0,0))
        setDisplay.blit(text,(500,50))

    elif q == 3:
        setDisplay.blit(pause,(0,0))
        font = pygame.font.SysFont("arial", 50)
        text = font.render("Score: " + str(c), True, white)
        setDisplay.blit(text,(500,50))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if (event.key == K_1):
                    q = 0
                elif (event.key == K_2):
                    pygame.quit()
                    sys.exit()
            
    pygame.display.update()
    fpsTime.tick(FPS)


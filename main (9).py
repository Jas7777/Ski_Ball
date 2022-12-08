import pygame
import random
import time
pygame.init()
ballx=250
bally=480
red=(250,0,0)
blue=(0,0,255)
yellow=(255,255,0)
black=(0,0,0)
color=black
screen = pygame.display.set_mode([500, 500])
running=True
Score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        value = random.randint(100,300)

        bally -= value
        time.sleep(0.1)
        if(value>250):
            print(" ")
        if(value>150):
            print(" ")
        if(value>100):
            print(" ")
    if pressed[pygame.K_RIGHT]:
        ballx += 1
    if pressed[pygame.K_LEFT]:
        ballx -= 1
    x = pygame.image.load('C:\\Users\\Sofy\\Downloads\\de.png')
    screen.blit(x, (0, 0))

    pygame.draw.circle(screen, color, (ballx,bally), 15)
    if(120<bally<180 and 100<ballx<160):
        color = red
      #  Score = Score + 100


    elif(120<bally<180 and 340<ballx<440):
        color = red
       # Score = Score + 100
        print(Score)

    if (bally < 150):
        color=red


    elif(bally<200):
        color=red
      #  Score=Score+50


    elif(bally<250):
        color=yellow
      #  Score = Score + 35


    elif(bally<340):
        color = blue
     #   Score = Score + 10











    pygame.display.update()

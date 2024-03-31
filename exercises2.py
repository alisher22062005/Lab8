import pygame
import sys

pygame.init()

screen=pygame.display.set_mode((400,600))
clock=pygame.time.Clock()
going=1

current_x=0
current_y=0
prev_x=0
prev_y=0

#colours
red=(255,0,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)


left_button_pressed=False

while going==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            going=0
            pygame.quit()

    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        print("hhh")
        current_x=event.pos[0]
        current_y=event.pos[1]
        prev_x=event.pos[0]
        prev_y=event.pos[1]
        left_button_pressed=True

    if event.type==pygame.MOUSEMOTION:
        print("Position of the mouse",event.pos)
        if left_button_pressed:
            #pygame.draw.rect(screen,(255,0,0),(event.pos[0],event.pos[1],5,5))
            current_x=event.pos[0]
            current_y=event.pos[1]
            pygame.draw.rect(screen,red,(prev_x,prev_y,current_x-prev_x,current_y-prev_y))


    if event.type==pygame.MOUSEBUTTONUP and event.button==1:
        left_button_pressed=False
        

    pygame.display.flip()
    clock.tick(60)
    
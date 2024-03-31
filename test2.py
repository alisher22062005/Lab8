import pygame, sys
import random, time
 
#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
 
#Create a white screen import pygame
 
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
 
game_over_font = pygame.font.SysFont('test2.py', 60)
 

game_over = game_over_font.render("Game Over", True, (255,0,0))
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
     
    screen.fill((255, 255, 255))
    screen.blit(game_over, (40,240))
     
    pygame.display.flip()
    clock.tick(60)
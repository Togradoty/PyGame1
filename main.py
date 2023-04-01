import pygame
import time
import sys
import os

#making a purple window
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
running = True
icon = pygame.image.load('Assets/128icon.png')
pygame.display.set_icon(icon)
#sets window title
pygame.display.set_caption("BadGame?")
white = (255, 255, 255)
Surface = (40, 40)
while running:
    #pygame.QUIT means user clicked X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #clears screen and fills with purple
    screen.fill("purple")

    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_ESCAPE:
            pygame.draw.rect(Surface, white)
        
        #if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            #running = False

    pygame.display.flip()
    clock.tick(24) #limits fps to 24

pygame.quit()
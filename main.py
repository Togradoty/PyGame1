import pygame
import time

#making a purple window
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

while running:
    #pygame.QUIT means user clicked X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #clears screen and fills with purple
    screen.fill("purple")
    #flip screen to put work on screen
    pygame.display.flip()

    clock.tick(60) #limits fps to 60

pygame.quit()
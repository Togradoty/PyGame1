import pygame
import time

#making a purple window
pygame.init()
screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
icon = pygame.image.load('Assets/128icon.png')
pygame.display.set_icon(icon)
#sets window title
pygame.display.set_caption("BadGame?")

while running:
    #pygame.QUIT means user clicked X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #clears screen and fills with purple
    screen.fill("purple")
    
    #changes to yellow if Y tapped
    if event.type == pygame.K_y:
        screen.fill("yellow")

    if event.type == pygame.K_ESCAPE:
        running = False

    pygame.display.flip()
    clock.tick(60) #limits fps to 60

pygame.quit()
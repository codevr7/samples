import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Click and drag to draw")
keep_going = True
COLOR = (random.randrange(0,255),random.randrange(0,255),
         random.randrange(0,255))
radius = 20
mousedown = True

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False

    if mousedown:
        spot = pygame.mouse.get_pos()
        pygame.draw.circle(screen, COLOR, spot, radius)
    pygame.display.update()
    
            
                           

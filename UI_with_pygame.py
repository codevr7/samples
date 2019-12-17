import pygame
import random

pygame.init()
screen = pygame.display.set_mode([800,600])

for i in range(100):
    color = (random.randint(0,255),random.randint(0,255)
                                 , random.randint(0,255))
    location = (random.randint(0,800))
    location_2 = (random.randint(0,600))
    sizes = random.randint(10,100)

    #for i in range(100):
    pygame.draw.circle(screen, color, (location,location_2), sizes)
    

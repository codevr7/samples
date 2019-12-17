import pygame
pygame.init()

# Setup of our present
screen = pygame.display.set_mode([800,800])
pygame.display.set_caption("Happy birthday")
keepGoing = True
screen_fill = False
V = (139,0,255)
I = (46,43,95)
B = (0,0,255)
G = (0,255,0)
Y = (255,255,0)
O = (255,127,0)
R = (255,0,0)
rectx = 790
recty = 790
rectw = 10
recth = 10

# The initial rectangle
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if pygame.key.get_pressed()[pygame.K_UP]:
            if screen_fill == False:
                pygame.draw.rect(screen,V,(rectx,recty,rectw,\
                                           recth))
                rectx -= 10
                recty -= 10
                rectw += 10
                recth += 10
    pygame.display.update()

pygame.quit()    


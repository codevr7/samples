# Importing the pygame for the use of the game
import pygame

pygame.init()# Initializing pygame

# The setup of the game
screen = pygame.display.set_mode([800,600])
pygame.display.set_caption("Kill the smiley")
keepGoing = True
pic = pygame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
launchx = 300
launchy = 350
orange = (255,140,0)
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
timer = pygame.time.Clock()
speedx = 5
speed_dir = 7
speed_up = 10
liney = 605
chances = 0
points = 0
#The initial position of our launcher
x1 = 385
x2 = 400
x3 = 415
y1 = 600
y2 = 585
y3 = 600
speed_up = 100
font = pygame.font.SysFont("Times", 24)
val_speed = 0        

# The game loop
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                points = 0
                chances = 0
                picx = 0
                liney = 605
                x1 = 385
                x2 = 400
                x3 = 415
                y1 = 600
                y2 = 585
                y3 = 600
                speedx = 5
                speed_dir = 7
                speed_up = 100
    screen.fill(black)
    launch = pygame.draw.polygon(screen,orange,((x1,y1),(x2,y2), (x3,y3)))    
    picx += speedx
    x1 += speed_dir
    x2 += speed_dir
    x3 += speed_dir
    screen.blit(pic,(picx,picy))
    
    # If the key - UP ARROW is pressed - bullet should move up
    if pygame.key.get_pressed()[pygame.K_UP]:
        linex = x2
        pygame.draw.rect(screen,red,(linex,liney,5,50))
        liney -= speed_up
        # Checking if user missed target
        if liney <= 0:
            liney = 605
            chances += 1
        # Checking if the bullet is hitting the smiley
        if liney + 2.5 <= picy + 100 and liney + 2.5 >= picy:
            if linex >= picx and linex <= picx + 100:
                points += 1
        print(chances - points)
    string = "Points :"  + str(points)
    miss_string = "Misses :" +  str(chances - points)
                   
    if chances - points == 3:
        speedx = 0
        speed_dir = 0
        speed_up = 0
        string = "Game over, your score was :" +  str(points)
        miss_string = "Press F1 to play again"
              
                
    if picx + pic.get_width() >= 800:
        speedx = -speedx-0.5
        val_speed += 1
        if val_speed == 12:
            print(1)
            speedx = -5
            val_speed = 0
    if picx <= 0:
        speedx = -speedx
    if x3 >= 800 or x1 <= 0:
        speed_dir = -speed_dir
        
    # Setting the points text location   
    text = font.render(string,True,white)
    text_rect = text.get_rect()
    text_rect.x = 1
    text_rect.y = screen.get_rect().centery

    # Setting the misses text location
    miss_text = font.render(miss_string,True,white)
    miss_rect = miss_text.get_rect()
    miss_rect.x = 1
    miss_rect.y = screen.get_rect().centery + 30

    screen.blit(miss_text,miss_rect)
    screen.blit(text,text_rect)
    timer.tick(60)
    pygame.display.update()
pygame.quit()

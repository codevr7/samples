import turtle
import random
t = turtle.Pen()
t.speed(10)
turtle.bgcolor("black")
colors = ["red","green","blue","gray","orange","purple","white","yellow"]
def spiral(x,y):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(90)
turtle.onscreenclick(spiral)        
    

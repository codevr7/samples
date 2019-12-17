import random
import turtle

t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red","blue","orange","green","gray","white","yellow","purple"]
for n in range(50):
    t.pencolor(random.choice(colors))
    size = random.randint(10,40)
    x = random.randrange(0,turtle.window_width()//2)
    y = random.randrange(0,turtle.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(90)
    t.penup()
    t.setpos(-x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(90)
    t.penup()
    t.setpos(-x,-y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(90)
    t.penup()
    t.setpos(x,-y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(90)

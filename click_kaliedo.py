import random
import turtle
t = turtle.Pen()
t.speed(10)
t.hideturtle()
turtle.bgcolor("black")
colors = ["red","blue","yellow","green","orange","gray","white","purple"]
def draw_kaleido(x,y):
    t.pencolor(random.choice(colors))
    size = random.randint(5,35)
    draw_spiral(x,y,size)
    draw_spiral(-x,y,size)
    draw_spiral(x,-y,size)
    draw_spiral(-x,-y,size)
def draw_spiral(x,y,size):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(90)
turtle.onscreenclick(draw_kaleido)        
    
    

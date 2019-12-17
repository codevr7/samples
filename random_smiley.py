import random
import turtle
t = turtle.Pen()
t.speed(10)
t.hideturtle()
turtle.bgcolor("black")
def draw_smiley(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()

    #head
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    #left eye
    t.setpos(x-15,y+60)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    #right eye
    t.setpos(x+15,y+60)
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    #mouth
    t.setpos(x-25,y+40)
    t.pencolor("black")
    t.width(10)
    t.goto(x-10,y+20)
    t.goto(x+10,y+20)
    t.width(1)

for n in range(50):
    x = random.randrange(-turtle.window_width()//2,
                         turtle.window_height()//2)
    y = random.randrange(-turtle.window_width()//2,
                         turtle.window_height()//2)
    draw_smiley(x,y)



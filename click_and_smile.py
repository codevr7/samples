import turtle
import random
t = turtle.Pen()
t.speed(10)
turtle.bgcolor("black")
def draw_smiley(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()

    #face
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    #left_eye
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
    t.goto(x+25,y+40)
    t.width(1)
turtle.onscreenclick(draw_smiley)    

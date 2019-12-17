import turtle
t = turtle.Pen()
t.speed(0)
turtle.onscreenclick(t.setpos)
b_g = input("what b_g color do you want to pick out of black,gray and white ? ")
if b_g == 'black':
    turtle.bgcolor("black")
elif b_g == 'gray':
    turtle.bgcolor('gray')
elif b_g == 'white':
    turtle.bgcolor("white")
else:
    print("given input not valid")
color = input("what color do you want out of red,blue green")
if color == 'red':
    t.pencolor("red")
elif color == 'green':
    t.pencolor("green")
elif color == 'blue':
    t.pencolor("blue")
else:
    t.pencolor("red")
    print("since you typed in an invalid passcode python in default python has put in red")

t.width(100)

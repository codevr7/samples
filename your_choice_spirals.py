import turtle
import random
password = input("type in the password ? ")
if password != 'arsenal':
    print("invalid password,try again or ask vishnu(or quit)")
while password != 'quit':
  if password == 'arsenal':
      background = input("choose your b-G colour between b/g/w ? ")
      t = turtle.Pen()
      if background == 'b':
        turtle.bgcolor("black")
      if background == 'w':
        turtle.bgcolor("white")
      if background == 'g':
        turtle.bgcolor("gray")
      colors = ['red','blue','green','yellow','orange','purple']
      shape = input("what shape do you want ,square or circle ? ")
      if shape == 'square':
          for n in range(50):
              t.pencolor(random.choice(colors))
              size = random.randint(10,40)
              x = random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
              y = random.randrange(-turtle.window_width()//2,turtle.window_width()//2)

              t.penup()
              t.setpos(x,y)
              t.pendown()
              for m in range(size):
                  t.forward(m*2)
                  t.left(90)
              
      if shape == 'circle':
          for n in range(50):
              t.pencolor(random.choice(colors))
              size = random.randint(10,40)
              x = random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
              y = random.randrange(-turtle.window_width()//2,turtle.window_width()//2)
              t.penup()
              t.setpos(x,y)
              t.pendown()
              t.circle(size)
          

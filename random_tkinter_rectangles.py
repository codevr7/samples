from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
def random_rectangle(width,height):
    X1 = random.randrange(width)
    Y1 = random.randrange(height)
    X2 = X1 + random.randrange(width)
    Y2 = Y1 + random.randrange(height)
    canvas.create_rectangle(X1,Y1,X2,Y2)
  

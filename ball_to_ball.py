from tkinter import *
import random
import time


class Ball:
    def __init__(self,canvas,target,color):
        self.canvas = canvas
        self.score = 0
        self.target = target
        self.id = canvas.create_oval(10,10,50,50,fill=color)
        self.canvas.move(self.id,245,100)
        starts = [-5,-4,-3,-2,-1,1,2,3,4,5]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -5
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>',self.move_up)
        self.canvas.bind_all('<KeyPress-Down>',self.move_down)
        self.hit_side = False
        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)    
        if pos[1] < 0:
            self.y = 0
            self.x = 0
            self.hit_side = True
        if pos[3] > self.canvas_height:    
            self.y = 0
            self.x = 0     
            self.hit_side = True
        if pos[0] < 0:
            self.x = 0
            self.y = 0
            self.hit_side = True
        if pos[2] > self.canvas_width:
            self.x = 0
            self.y = 0
            self.hit_side = True
       
        if self.hit_side == True:
            canvas.create_text(self.canvas_width/2,self.canvas_height/2,text = ("Your score is %s" % ball.score ),font = ('times',40))
            sys.exit()

    def check_target(self):
        pos = self.canvas.coords(self.id)    
        tar_pos = self.canvas.coords(self.target.id)
        if pos[0] <= tar_pos[2] and pos[2] >= tar_pos[0]:
            if pos[3] >= tar_pos[1] and pos[3] <= tar_pos[3]:
                return True
        return False
        
    def turn_left(self,evt):
        self.x = -10
        self.y = 0
    def turn_right(self,evt):
        self.x = 10
        self.y = 0
    def move_up(self,evt):
        self.y = -10
        self.x = 0
    def move_down(self,evt):
        self.y = 10
        self.x = 0

class Target:

    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(100,100,110,110,fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.x = 0 #initialize
        self.y = 0 #initialize

    def random_draw(self):
        self.x = random.randrange(0,self.canvas_width) 
        self.y = random.randrange(0,self.canvas_height)
        self.canvas.move(self.id,self.x ,self.y)
        tar_pos = self.canvas.coords(self.id)
        x = self.x - tar_pos[0] 
        y = self.y - tar_pos[1]
        self.canvas.move(self.id,x,y)

class Score:
    def __init__(self,canavs):
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.id = Label(canvas,text = "Score = 0")
        self.id.place(x = 600 , y = 20)

    def draw(self,score):
        self.id["text"] = "Score = %s" % (ball.score)
        
        
tk = Tk()
tk.title("ball to ball")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width = 700,height = 500,bd = 1,highlightthickness = 0)
canvas.pack()
tk.update()


target = Target(canvas,'blue')
ball = Ball(canvas,target,'red')
target.random_draw()
score = Score(canvas)



while 1:
    if ball.hit_side == False:
        ball.draw()
    if ball.check_target() == True:
        score.draw(ball.score)
        ball.score += 1
        target.random_draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.05)

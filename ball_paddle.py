from tkinter import *
import random
import time

class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas = canvas
        self.paddle = paddle
        self.score = 0
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.score = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.lives = 1
        self.restart = False
        

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False 
  
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            self.lives -= 1
        if self.hit_paddle(pos) == True:
            self.y = -3
            self.score = self.score + 1    
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        if self.lives == 0:
            self.text_1 = canvas.create_text(self.canvas_width/2,self.canvas_height/2,\
                text = ("Your score is:  %s" % ball.score),font = ('courier',22))
            self.text_2 = canvas.create_text(self.canvas_width/2,self.canvas_height/2+50,\
                text = ("Press the UP ARROW to play again"),font = ('courier',15))
            self.canvas.bind_all('<KeyPress-Up>',self.restart_game)
    def restart_game(self,evt):
        if self.hit_bottom == True:
            pos = self.canvas.coords(self.id)
            self.lives = 1
            self.score = 0
            self.hit_bottom = False
            self.canvas.move(self.id,-pos[0],-300)
            self.restart = True
    def delete_text1(self):
        self.canvas.delete(self.text_1)
    def delete_text2(self):
        self.canvas.delete(self.text_2)
        

class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self,evt):
        self.x = -5
    def turn_right(self,evt):
        self.x = 5

class Score:
    def __init__(self,canvas):
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.id = Label(canvas,text = "Score = 0")
        self.id.place(x = self.canvas_width - 90, y = 20)
        
    def draw(self,score):
        self.id['text'] = "Score = %s" % (score)
   
tk = Tk() 
tk.title("game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width = 500,height = 400,bd = 0,highlightthickness = 0)
canvas.pack()
tk.update()

paddle = Paddle(canvas,'blue')
ball = Ball(canvas,paddle,'red')
score = Score(canvas)

while 1:
    if ball.hit_bottom == False:      
        ball.draw()
        paddle.draw()
        score.draw(ball.score)
    if ball.restart == True:
        ball.delete_text1()
        ball.delete_text2()
        ball.restart = False
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
   

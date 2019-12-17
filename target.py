from tkinter import *
import random
import time

class Launch:
    def __init__(self,canvas,target,color, control):
        self.canvas = canvas
        self.target = target
        self.control = control
        self.id = canvas.create_polygon(100,100,110,90,120,100,fill=color)
        self.canvas.move(self.id,381,280)
        self.x = 0
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Up>',self.move_up)
        self.miss = False
        self.pos = self.canvas.coords(self.id)
        self.game_over = False

    def reset(self):
        self.canvas.move(self.id, -1 * self.pos[0],self.canvas_height - self.pos[1])
        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        self.pos = self.canvas.coords(self.id)
        if self.pos[4] >= self.canvas_width:
            self.x = -3
        elif self.pos[0] <= 0:
            self.x = 3
        if self.hit_target(self.pos) == True:
            self.y = 0
            self.x = 0
            target.x = 0
            self.text1_id = canvas.create_text(self.canvas_width/2,self.canvas_height/2,text =
                    ("You hit your target...Booyah!!!"),font = ('courier',10))
        if self.pos[3] <= 0:
            self.game_over = True
            self.control.run = False
            self.y = 0
            self.text2_id = canvas.create_text(self.canvas_width/2,self.canvas_height/2,text =
                    ("You missed your target ..."),font = ('courier',10))
    def delete_text1(self):
        self.canvas.delete(self.text1_id)
        
    def delete_text2(self):     
        self.canvas.delete(self.text2_id)
        
    def move_up(self,evt):
        self.y = -5
        self.x = 0

    def hit_target(self,pos):
        target_pos = self.canvas.coords(self.target.id)
        if pos[3] >= target_pos[1] and pos[3] <= target_pos[3]:
            if pos[0] >= target_pos[0] and pos[4] <= target_pos[2]:
                return True
        return False    

class Target:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(10,10,80,20,fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.x = 0
        self.y = 0
        self.pos = self.canvas.coords(self.id)
        self.reset()

    def reset(self):
        self.canvas.move(self.id,self.canvas_width - self.pos[0],0)
        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        self.pos = self.canvas.coords(self.id)
        if self.pos[0] <= 0:
            self.x = 2
        elif self.pos[2] >= self.canvas_width:
            self.x = -2

class GameControl:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.bind_all('<space>',self.restart)
        self.do_restart = False
        self.run = True

    def restart(self, evt):
        self.do_restart = True
        
tk = Tk()
tk.title("Target")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack()
tk.update()

control = GameControl(canvas)
target = Target(canvas, 'red')
launch = Launch(canvas, target, 'green', control)

while 1:
    if control.do_restart == True:
        control.do_restart = False
        target.reset()
        launch.reset()
        if launch.hit_target == True:
            launch.delete_text1()
        if launch.game_over:
            launch.delete_text2()
        control.run = True
    if control.run == True:
        launch.draw()
        target.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

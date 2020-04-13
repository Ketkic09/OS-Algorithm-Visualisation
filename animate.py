from tkinter import *

import random
import time

def ball():
    xspeed=9
    yspeed=0
    ball1=canvas.create_oval(100,300,150,250,fil="red")
    ball2=canvas.create_oval(200,300,250,250,fil="red")
    ball3=canvas.create_oval(300,300,350,250,fil="red")
    while True:
        canvas.move(ball3,xspeed,yspeed)
        pos=canvas.coords(ball3)
        if pos[3]>=1000 or pos[1]<=0:
            yspeed=-yspeed
        if pos[2]>=800 or pos[0]<=0:
            break
        tk.update()
        time.sleep(0.1)

        
    while True:
        canvas.move(ball2,xspeed,yspeed)
        pos=canvas.coords(ball2)
        if pos[3]>=1000 or pos[1]<=0:
            yspeed=-yspeed
        if pos[2]>=500 or pos[0]<=0:
            break
    
        tk.update()
        time.sleep(0.1)

tk=Tk()
tk.title("Graphics")

Height=1000
Width=1000
canvas=Canvas(tk,width=Width,height=Height)
canvas.pack()



bt1=Button(tk, text="START", width=8, command=ball)
bt1.place(x=800,y=500)

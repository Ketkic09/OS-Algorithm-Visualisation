  
from tkinter import *

import random
import time



def ball():
    xspeed=9
    yspeed=0
    x1=9
    y1=0 
    c= '10'
    d = '20'
    e='30'
    f='40'
    g='50'
    canvas.create_rectangle(200,100,500,150,outline="#fb0",fill="#fb0")
    canvas.create_rectangle(700,100,900,400,outline="#fb0",fill="#fb0")
    ball1=canvas.create_oval(100,300,150,250,fil="red")
    ball2=canvas.create_oval(200,300,250,250,fil="red")
    ball3=canvas.create_oval(300,300,350,250,fil="red")
    ball4=canvas.create_oval(400,300,450,250,fill="red")
    ball5=canvas.create_oval(500,300,550,250,fill="red")
    text5=canvas.create_text(525,275,text=c,font=18)
    text4=canvas.create_text(425,275,text=d,font=18)
    text3=canvas.create_text(325,275,text=e,font=18)
    text2=canvas.create_text(225,275,text=f,font=18)
    text1=canvas.create_text(125,275,text=g,font=18)
    while True:
        canvas.move(ball5,xspeed,yspeed)
        canvas.move(text5,x1,y1)
        pos1=canvas.coords(text5)
        pos=canvas.coords(ball5)
        if pos[3]>=1000 or pos[1]<=0:
            yspeed=-yspeed
            y1=-y1
        if pos[2]>=800 or pos[0]<=0:
            canvas.delete(ball5)
            canvas.delete(text5)
            break
            
        tk.update()
        time.sleep(0.1)
    global val
    val = int(c) + val  
    t1=canvas.create_text(350,130,text=val,font=18)
    
    while True:
        canvas.move(ball4,xspeed,yspeed)
        pos=canvas.coords(ball4)
        canvas.move(text4,x1,y1)
        pos1=canvas.coords(text4)
        if pos[3]>=1000 or pos[1]<=0:
            yspeed=-yspeed
            y1=-y1
        if pos[2]>=800 or pos[0]<=0:
            canvas.delete(ball4)
            canvas.delete(text4)
            break
        tk.update()
        time.sleep(0.1)
    canvas.delete(t1)
    val = int(d) + val  
    t1=canvas.create_text(350,130,text=val,font=18)
       
    while True:
        canvas.move(ball3,xspeed,yspeed)
        pos=canvas.coords(ball3)
        canvas.move(text3,x1,y1)
        pos1=canvas.coords(text3)
        if pos[3]>=1000 or pos[1]<=0:
            yspeed=-yspeed
            y1=-y1
        if pos[2]>=800 or pos[0]<=0:
            canvas.delete(ball3)
            canvas.delete(text3)
            break
        tk.update()
        time.sleep(0.1)
    canvas.delete(t1)
    val = int(e) + val  
    t1=canvas.create_text(350,130,text=val,font=18)

        
    while True:
        canvas.move(ball2,xspeed,yspeed)
        pos=canvas.coords(ball2)
        canvas.move(text2,x1,y1)
        pos1=canvas.coords(text2)
        if pos[3]>=1000 or pos[1]<=0:
            yspeed=-yspeed
            y1=-y1
        if pos[2]>=800 or pos[0]<=0:
            canvas.delete(ball2)
            canvas.delete(text2)
            break
        tk.update()
        time.sleep(0.1)
    canvas.delete(t1)
    val = int(f) + val  
    t1=canvas.create_text(350,130,text=val,font=18)
    canvas.delete(t1)
    while True:
        canvas.move(ball1,xspeed,yspeed)
        pos=canvas.coords(ball1)
        canvas.move(text1,x1,y1)
        pos1=canvas.coords(text1)
        if pos[3]>=1000 or pos[1]<=0:
            yspeed=-yspeed
            y1=-y1
        if pos[2]>=800 or pos[0]<=0:
            canvas.delete(ball1)
            canvas.delete(text1)
            break
        tk.update()
        time.sleep(0.1)
    canvas.delete(t1)
    val = int(g) + val  
    t1=canvas.create_text(350,130,text=val,font=18)
    val = val/5
    t2=canvas.create_text(350,200,text='Average waiting time : '+str(val),font=18)


    
tk=Tk()
tk.title("Graphics")

Height=1000
Width=1000
canvas=Canvas(tk,width=Width,height=Height)
canvas.pack()


val = 0



bt1=Button(tk, text="START", width=8, command=ball)
bt1.place(x=800,y=500)

tk.mainloop()
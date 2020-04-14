from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
import random
import time


root = Tk()
root.title('OS algorithm visualisation ')
root.geometry('1450x800')
root.configure(bg="tomato")
val = 0
global e1,e2,e3,e4,e5,y1,y2,y3,y4,y5
def ball():
    tk=Tk()
    tk.title("Graphics")
    Height=1000
    Width=1000
    canvas=Canvas(tk,width=Width,height=Height)
    canvas.pack()
    xspeed=9
    yspeed=0
    x1=9
    y11=0

    canvas.create_rectangle(200,100,300,150,outline="#fb0",fill="#fb0") #change position of this rectangle and accordingly change the postion of the text
    canvas.create_rectangle(700,100,900,400,outline="#fb0",fill="#fb0")
    ball1=canvas.create_oval(100,300,150,250,fil="red")
    ball2=canvas.create_oval(200,300,250,250,fil="red")
    ball3=canvas.create_oval(300,300,350,250,fil="red")
    ball4=canvas.create_oval(400,300,450,250,fill="red")
    ball5=canvas.create_oval(500,300,550,250,fill="red")
    text5=canvas.create_text(525,275,text=y1,font=18)
    text4=canvas.create_text(425,275,text=y2,font=18)
    text3=canvas.create_text(325,275,text=y3,font=18)
    text2=canvas.create_text(225,275,text=y4,font=18)
    text1=canvas.create_text(125,275,text=y5,font=18)
    while True:
        canvas.move(ball5,xspeed,yspeed)
        canvas.move(text5,x1,y11)
        pos1=canvas.coords(text5)
        pos=canvas.coords(ball5)
        if pos[3]>=1000 or pos[1]<=0:
            yspeed=-yspeed
            y11=-y11
        if pos[2]>=800 or pos[0]<=0:
            canvas.delete(ball5)
            canvas.delete(text5)
            break
        tk.update()
        time.sleep(0.1)
    global val
    val = int(y1) + val 
    t1=canvas.create_text(250,130,text=val,font=18) 
    
    while True:
        canvas.move(ball4,xspeed,yspeed)
        pos=canvas.coords(ball4)
        canvas.move(text4,x1,y11)
        pos1=canvas.coords(text4)
        if pos[3]>=1000 or pos[1]<=0:
            yspeed=-yspeed
            y11=-y11
        if pos[2]>=800 or pos[0]<=0:
            canvas.delete(ball4)
            canvas.delete(text4)
            break
        tk.update()
        time.sleep(0.1)
    canvas.delete(t1)
    val = int(y2) + val 
    t1=canvas.create_text(250,130,text=val,font=18)
        
    while True:
        canvas.move(ball3,xspeed,yspeed)
        pos=canvas.coords(ball3)
        canvas.move(text3,x1,y11)
        pos1=canvas.coords(text3)
        if pos[3]>=1000 or pos[1]<=0:
            yspeed=-yspeed
            y11=-y11
        if pos[2]>=800 or pos[0]<=0:
            canvas.delete(ball3)
            canvas.delete(text3)
            break
        tk.update()
        time.sleep(0.1)
    canvas.delete(t1)
    val = int(y3) + val 
    t1=canvas.create_text(250,130,text=val,font=18)
        
    while True:
        canvas.move(ball2,xspeed,yspeed)
        pos=canvas.coords(ball2)
        canvas.move(text2,x1,y11)
        pos1=canvas.coords(text2)
        if pos[3]>=1000 or pos[1]<=0:
            yspeed=-yspeed
            y11=-y11
        if pos[2]>=800 or pos[0]<=0:
            canvas.delete(ball2)
            canvas.delete(text2)
            break
        tk.update()
        time.sleep(0.1)
    canvas.delete(t1)
    val = int(y4) + val 
    t1=canvas.create_text(250,130,text=val,font=18)
    while True:
        canvas.move(ball1,xspeed,yspeed)
        pos=canvas.coords(ball1)
        canvas.move(text1,x1,y11)
        pos1=canvas.coords(text1)
        if pos[3]>=1000 or pos[1]<=0:
            yspeed=-yspeed
            y11=-y11
        if pos[2]>=800 or pos[0]<=0:
            canvas.delete(ball1)
            canvas.delete(text1)
            break
        tk.update()
        time.sleep(0.1)
    canvas.delete(t1)
    val = int(y5) + val 
    t1=canvas.create_text(250,130,text=val,font=18)
    
    val = val/5
    t2=canvas.create_text(300,200,text='Average waiting time : '+str(val),font=18)

def vis1():
    tk=Tk()
    tk.title("Graphics")

    Height=1000
    Width=1000
    canvas=Canvas(tk,width=Width,height=Height)
    canvas.pack()



    bt1=Button(tk, text="START", width=10, command=ball)
    bt1.place(x=500,y=500)
    
def vis2():
    sj=[]
    tk=Tk()
    tk.title("Graphics")

    Height=1000
    Width=1000
    canvas=Canvas(tk,width=Width,height=Height)
    canvas.pack()
    v1=Label(master=tk,text="Values entered by the user",fg="green",font=("helvetica",15,"bold"))
    v1.place(x=100,y=155)
    ball1=canvas.create_oval(100,300,150,250,fil="red")
    ball2=canvas.create_oval(200,300,250,250,fil="red")
    ball3=canvas.create_oval(300,300,350,250,fil="red")
    ball4=canvas.create_oval(400,300,450,250,fill="red")
    ball5=canvas.create_oval(500,300,550,250,fill="red")
    text5=canvas.create_text(525,275,text=y1,font=18)
    text4=canvas.create_text(425,275,text=y2,font=18)
    text3=canvas.create_text(325,275,text=y3,font=18)
    text2=canvas.create_text(225,275,text=y4,font=18)
    text1=canvas.create_text(125,275,text=y5,font=18)
    v2=Label(master=tk,text="In SJF the shortest job needs to be execute first Hence we will sort them in ascending order",fg="green",font=("helvetica",15,"bold"))
    v2.place(x=100,y=350)
    v3=Label(master=tk,text="Click the button to arrange them in ascending order and visualization:",fg="green",font=("helvetica",15,"bold"))
    v3.place(x=100,y=400)
    sj.append(y1)
    sj.append(y2)
    sj.append(y3)
    sj.append(y4)
    sj.append(y5)
    sj.sort()
    def ball1():
        xspeed=9
        yspeed=0
        print(sj)
        x1=9
        y11=0
        canvas.create_rectangle(200,100,300,150,outline="#fb0",fill="#fb0") #change position of this rectangle and accordingly change the postion of the text
        canvas.create_rectangle(700,500,900,650,outline="#fb0",fill="#fb0")
        ball1=canvas.create_oval(100,550,150,600,fil="red")
        ball2=canvas.create_oval(200,550,250,600,fil="red")
        ball3=canvas.create_oval(300,550,350,600,fil="red")
        ball4=canvas.create_oval(400,550,450,600,fill="red")
        ball5=canvas.create_oval(500,550,550,600,fill="red")
        text5=canvas.create_text(525,575,text=sj[0],font=18)
        text4=canvas.create_text(425,575,text=sj[1],font=18)
        text3=canvas.create_text(325,575,text=sj[2],font=18)
        text2=canvas.create_text(225,575,text=sj[3],font=18)
        text1=canvas.create_text(125,575,text=sj[4],font=18)
        while True:
            canvas.move(ball5,xspeed,yspeed)
            canvas.move(text5,x1,y11)
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
        val = int(sj[0])+val
        t1=canvas.create_text(250,130,text=val,font=18)

        while True:
            canvas.move(ball4,xspeed,yspeed)
            pos=canvas.coords(ball4)
            canvas.move(text4,x1,y11)
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
        val = int(sj[1])+val
        t1=canvas.create_text(250,130,text=val,font=18)

        while True:
            canvas.move(ball3,xspeed,yspeed)
            pos=canvas.coords(ball3)
            canvas.move(text3,x1,y11)
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
        val = int(sj[2])+val
        t1=canvas.create_text(250,130,text=val,font=18)
            
        while True:
            canvas.move(ball2,xspeed,yspeed)
            pos=canvas.coords(ball2)
            canvas.move(text2,x1,y11)
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
        val = int(sj[3])+val
        t1=canvas.create_text(250,130,text=val,font=18)
        while True:
            canvas.move(ball1,xspeed,yspeed)
            pos=canvas.coords(ball1)
            canvas.move(text1,x1,y11)
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
        val = int(sj[4])+val
        t1=canvas.create_text(250,130,text=val,font=18)
        val = val/5
        t2=canvas.create_text(299,200,text='Average waiting time : '+str(val),font=18)
    bt1=Button(tk, text="START", width=8, command=ball1)
    bt1.place(x=800,y=400)
def clear1():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
def totale1():
    window=Tk()
    window.geometry("1450x800")
    window.title("SJF")
    window.configure(bg="tomato")
    title=Label(master=window,text="SJF",bg="YELLOW",fg="green",font=("helvetica",70,"bold"))
    title.place(x=1000,y=90)
    global e1,e2,e3,e4,e5,y1,y2,y3,y4,y5
    n=5
    if(e1.get()==""):
        y1=0
    else:
        y1=int(e1.get())
    if(e2.get()==""):
        y2=0
    else:
        y2=int(e2.get())
    if(e3.get()==""):
        y3=0
    else:
        y3=int(e3.get())
    if(e4.get()==""):
        y4=0
    else:
        y4=int(e4.get())
    if(e5.get()==""):
        y5=0
    else:
        y5=int(e5.get())

    
    p=[]
    for i in range(0,n):
        p.insert(i,i+1)
        
    bt=[]
    bt.append(y1)
    bt.append(y2)
    bt.append(y3)
    bt.append(y4)
    bt.append(y5)
    
    wt=[]   
    avgwt=0
    tat=[]
    avgtat=0
    wt.insert(0,0)
    tat.insert(0,bt[0])
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if(bt[j]>bt[j+1]):
                temp=bt[j]
                bt[j]=bt[j+1]
                bt[j+1]=temp
                temp=p[j]
                p[j]=p[j+1]
                p[j+1]=temp
   
       
    for i in range(1,n):
        wt.insert(i,wt[i-1]+bt[i-1])
        avgwt+=wt[i]
    
         
         
    for i in range(0,n):
        
        tat.insert(i,wt[i]+bt[i])
        avgtat+=tat[i]

    avgwt=float(avgwt)/n
    avgtat=float(avgtat)/n
    
    w1=Label(master=window,text=wt[0],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w1.place(x=575,y=155)
    w2=Label(master=window,text=wt[1],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w2.place(x=575,y=255)
    w3=Label(master=window,text=wt[2],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w3.place(x=575,y=355)
    w4=Label(master=window,text=wt[3],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w4.place(x=575,y=455)
    w5=Label(master=window,text=wt[4],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w5.place(x=575,y=555)
        
   
    for i in range(0,n):
        t1=Label(master=window,text=tat[0],bg="tomato",fg="green",font=("helvetica",25,"bold"))
        t1.place(x=775,y=155)
        t2=Label(master=window,text=tat[1],bg="tomato",fg="green",font=("helvetica",25,"bold"))
        t2.place(x=775,y=255)
        t3=Label(master=window,text=tat[2],bg="tomato",fg="green",font=("helvetica",25,"bold"))
        t3.place(x=775,y=355)
        t4=Label(master=window,text=tat[3],bg="tomato",fg="green",font=("helvetica",25,"bold"))
        t4.place(x=775,y=455)
        t5=Label(master=window,text=tat[4],bg="tomato",fg="green",font=("helvetica",25,"bold"))
        t5.place(x=775,y=555)

    
    for i in range(0,n):
        l1=Label(master=window,text=p[0],bg="tomato",fg="green",font=("helvetica",25,"bold"))
        l1.place(x=200,y=155)
        l2=Label(master=window,text=p[1],bg="tomato",fg="green",font=("helvetica",25,"bold"))
        l2.place(x=200,y=255)
        l3=Label(master=window,text=p[2],bg="tomato",fg="green",font=("helvetica",25,"bold"))
        l3.place(x=200,y=355)
        l4=Label(master=window,text=p[3],bg="tomato",fg="green",font=("helvetica",25,"bold"))
        l4.place(x=200,y=455)
        l5=Label(master=window,text=p[4],bg="tomato",fg="green",font=("helvetica",25,"bold"))
        l5.place(x=200,y=555)
        
    

    for i in range(0,n):
         q1=Label(master=window,text=bt[0],bg="tomato",fg="green",font=("helvetica",25,"bold"))
         q1.place(x=375,y=155)
         q2=Label(master=window,text=bt[1],bg="tomato",fg="green",font=("helvetica",25,"bold"))
         q2.place(x=375,y=255)
         q3=Label(master=window,text=bt[2],bg="tomato",fg="green",font=("helvetica",25,"bold"))
         q3.place(x=375,y=355)
         q4=Label(master=window,text=bt[3],bg="tomato",fg="green",font=("helvetica",25,"bold"))
         q4.place(x=375,y=455)
         q5=Label(master=window,text=bt[4],bg="tomato",fg="green",font=("helvetica",25,"bold"))
         q5.place(x=375,y=555)
                
    awt=Label(master=window,text="Average waiting time:",bg="tomato",fg="green",font=("helvetica",20,"bold"))
    awt.place(x=890,y=300)
    awta=Label(master=window,text=avgwt,bg="tomato",fg="green",font=("helvetica",20,"bold"))
    awta.place(x=1190,y=300)
    tatb=Label(master=window,text="Average turn around time:",bg="tomato",fg="green",font=("helvetica",20,"bold"))
    tatb.place(x=890,y=400)
    tata=Label(master=window,text=avgtat,bg="tomato",fg="green",font=("helvetica",20,"bold"))
    tata.place(x=1250,y=400)
    total=Button(master=window,text="CALCULATE",bg="white",command=totale1,fg="green",font=("helvetica",15,"bold"))
    total.place(x=525,y=650)
    m0=Label(master=window,text="BRUST TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m0.place(x=20,y=80)

    m1=Label(master=window,text="PROCESSES",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m1.place(x=170,y=80)
    m2=Label(master=window,text="NEW TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m2.place(x=320,y=80)
    m3=Label(master=window,text="WAITING TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m3.place(x=500,y=80)

    m4=Label(master=window,text="TURN AROUND TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m4.place(x=700,y=80)



    e1=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e1.place(x=50,y=155)
    e2=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e2.place(x=50,y=255)
    e3=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e3.place(x=50,y=355)
    e4=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e4.place(x=50,y=455)
    e5=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e5.place(x=50,y=555)
    e1.insert(END,y1)
    e2.insert(END,y2)
    e3.insert(END,y3)
    e4.insert(END,y4)
    e5.insert(END,y5)
    clear=Button(master=window,text="CLEAR",bg="white",command=clear1,fg="red",font=("helvetica",15,"bold"))
    clear.place(x=800,y=650)
    vis=Button(master=window,text="VISUALIZATION",bg="white",command=vis2,fg="red",font=("helvetica",15,"bold"))
    vis.place(x=1075,y=650)
def totale2():
    n=5
    wt=[]
    tat=[]
    global e1,e2,e3,e4,e5,y1,y2,y3,y4,y5
    if(e1.get()==""):
        y1=0
    else:
        y1=int(e1.get())
    if(e2.get()==""):
        y2=0
    else:
        y2=int(e2.get())
    if(e3.get()==""):
        y3=0
    else:
        y3=int(e3.get())
    if(e4.get()==""):
        y4=0
    else:
        y4=int(e4.get())
    if(e5.get()==""):
        y5=0
    else:
        y5=int(e5.get())
        
    if(s1.get()==""):
        v1=0
    else:
        v1=int(s1.get())
    if(s2.get()==""):
        v2=0
    else:
        v2=int(s2.get())
    if(s3.get()==""):
        v3=0
    else:
        v3=int(s3.get())
    if(s4.get()==""):
        v4=0
    else:
        v4=int(s4.get())
    if(s5.get()==""):
        v5=0
    else:
        v5=int(s5.get())
    priority=[]
    priority.append(y1)
    priority.append(y2)
    priority.append(y3)
    priority.append(y4)
    priority.append(y5)
    print(priority)
    bt=[]
    bt.append(v1)
    bt.append(v2)
    bt.append(v3)
    bt.append(v3)
    bt.append(v3)
    print(bt)
    processes=[]
    for i in range(0,n):
        processes.insert(i,i+1)
    for i in range(0,len(priority)-1):
        for j in range(0,len(priority)-i-1):
            if(priority[j]>priority[j+1]):
                swap=priority[j]
                priority[j]=priority[j+1]
                priority[j+1]=swap
                swap=bt[j]
                bt[j]=bt[j+1]
                bt[j+1]=swap
                swap=processes[j]
                processes[j]=processes[j+1]
                processes[j+1]=swap
    wt.insert(0,0)
    tat.insert(0,bt[0])
    for i in range(1,len(processes)):
        wt.insert(i,wt[i-1]+bt[i-1])
        tat.insert(i,wt[i]+bt[i])
        avgtat=0
        avgwt=0
    for i in range(0,len(processes)):
        avgwt=avgwt+wt[i]
        avgtat=avgtat+tat[i]
    avgwt=float(avgwt)/n
    avgtat=float(avgtat)/n
    print(avgwt)
    print(avgtat)
    t1=Label(master=window,text=wt[0],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t1.place(x=575,y=155)
    t2=Label(master=window,text=wt[1],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t2.place(x=575,y=255)
    t3=Label(master=window,text=wt[2],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t3.place(x=575,y=355)
    t4=Label(master=window,text=wt[3],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t4.place(x=575,y=455)
    t5=Label(master=window,text=wt[4],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t5.place(x=575,y=555)
    o1=Label(master=window,text=tat[0],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o1.place(x=775,y=155)
    o2=Label(master=window,text=tat[1],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o2.place(x=775,y=255)
    o3=Label(master=window,text=tat[2],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o3.place(x=775,y=355)
    o4=Label(master=window,text=tat[3],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o4.place(x=775,y=455)
    o5=Label(master=window,text=tat[4],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o5.place(x=775,y=555)
    awta=Label(master=window,text=avgwt,bg="tomato",fg="green",font=("helvetica",15,"bold"))
    awta.place(x=1180,y=300)
    tata=Label(master=window,text=avgtat,bg="tomato",fg="green",font=("helvetica",15,"bold"))
    tata.place(x=1230,y=400)
    total=Button(master=window,text="CALCULATE",bg="white",command=totale2,fg="green",font=("helvetica",15,"bold"))
    total.place(x=525,y=650)

def totale():
    window=Tk()
    window.geometry("1450x800")
    window.title("FCFS")
    window.configure(bg="tomato")
    global e1,e2,e3,e4,e5,y1,y2,y3,y4,y5
    n=5
    if(e1.get()==""):
        y1=0
    else:
        y1=int(e1.get())
    if(e2.get()==""):
        y2=0
    else:
        y2=int(e2.get())
    if(e3.get()==""):
        y3=0
    else:
        y3=int(e3.get())
    if(e4.get()==""):
        y4=0
    else:
        y4=int(e4.get())
    if(e5.get()==""):
        y5=0
    else:
        y5=int(e5.get())
    bt=[]
    bt.append(y1)
    bt.append(y2)
    bt.append(y3)
    bt.append(y4)
    bt.append(y5)
    wt=[]   
    avgwt=0
    tat=[]
    avgtat=0
    wt.insert(0,0)
    tat.insert(0,bt[0])
    for i in range(1,n):
        wt.insert(i,wt[i-1]+bt[i-1])
        tat.insert(i,wt[i]+bt[i])
        avgwt+=wt[i]
    avgwt=float(avgwt)/n
    for i in range(0,n):
        avgtat+=tat[i]
    
    avgtat=float(avgtat)/n
    w1=Label(master=window,text=wt[0],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w1.place(x=375,y=155)
    w2=Label(master=window,text=wt[1],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w2.place(x=375,y=255)
    w3=Label(master=window,text=wt[2],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w3.place(x=375,y=355)
    w4=Label(master=window,text=wt[3],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w4.place(x=375,y=455)
    w5=Label(master=window,text=wt[4],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w5.place(x=375,y=555)
    t1=Label(master=window,text=tat[0],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t1.place(x=575,y=155)
    t2=Label(master=window,text=tat[1],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t2.place(x=575,y=255)
    t3=Label(master=window,text=tat[2],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t3.place(x=575,y=355)
    t4=Label(master=window,text=tat[3],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t4.place(x=575,y=455)
    t5=Label(master=window,text=tat[4],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t5.place(x=575,y=555)
    awt=Label(master=window,text="Average waiting time:",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    awt.place(x=775,y=300)
    awta=Label(master=window,text=avgwt,bg="tomato",fg="green",font=("helvetica",25,"bold"))
    awta.place(x=1150,y=300)
    tatb=Label(master=window,text="Average turn around time:",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    tatb.place(x=775,y=400)
    tata=Label(master=window,text=avgtat,bg="tomato",fg="green",font=("helvetica",25,"bold"))
    tata.place(x=1200,y=400)
    total=Button(master=window,text="CALCULATE",bg="white",command=totale,fg="green",font=("helvetica",15,"bold"))
    total.place(x=525,y=650)
    title=Label(master=window,text="FCFS",bg="YELLOW",fg="green",font=("helvetica",70,"bold"))
    title.place(x=900,y=90)
    m1=Label(master=window,text="BURST TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m1.place(x=130,y=80)
    m2=Label(master=window,text="WAITING TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m2.place(x=320,y=80)
    m3=Label(master=window,text="TURN AROUND TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m3.place(x=500,y=80)
    e1=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e1.place(x=175,y=155)
    e2=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e2.place(x=175,y=255)
    e3=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e3.place(x=175,y=355)
    e4=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e4.place(x=175,y=455)
    e5=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e5.place(x=175,y=555)
    e1.insert(END,y1)
    e2.insert(END,y2)
    e3.insert(END,y3)
    e4.insert(END,y4)
    e5.insert(END,y5)
    l1=Label(master=window,text="PROCESS 1 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l1.place(x=20,y=155)
    l2=Label(master=window,text="PROCESS 2 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l2.place(x=20,y=255)
    l3=Label(master=window,text="PROCESS 3 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l3.place(x=20,y=355)
    l4=Label(master=window,text="PROCESS 4 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l4.place(x=20,y=455)
    l5=Label(master=window,text="PROCESS 5 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l5.place(x=20,y=555)
    clear=Button(master=window,text="CLEAR",bg="white",command=clear1,fg="red",font=("helvetica",15,"bold"))
    clear.place(x=800,y=650)
    vis=Button(master=window,text="VISUALIZATION",bg="white",command=vis1,fg="red",font=("helvetica",15,"bold"))
    vis.place(x=1075,y=650)
    
def fcfsb():
    window=Tk()
    window.geometry("1450x800")
    window.title("FCFS")
    window.configure(bg="tomato")
    wait=15
    global e1,e2,e3,e4,e5,y1,y2,y3,y4,y5
    title=Label(master=window,text="FCFS",bg="YELLOW",fg="green",font=("helvetica",70,"bold"))
    title.place(x=900,y=90)
    m1=Label(master=window,text="BURST TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m1.place(x=130,y=80)
    m2=Label(master=window,text="WAITING TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m2.place(x=320,y=80)
    m3=Label(master=window,text="TURN AROUND TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m3.place(x=500,y=80)
    e1=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e1.place(x=175,y=155)
    e2=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e2.place(x=175,y=255)
    e3=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e3.place(x=175,y=355)
    e4=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e4.place(x=175,y=455)
    e5=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e5.place(x=175,y=555)
    l1=Label(master=window,text="PROCESS 1 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l1.place(x=20,y=155)
    l2=Label(master=window,text="PROCESS 2 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l2.place(x=20,y=255)
    l3=Label(master=window,text="PROCESS 3 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l3.place(x=20,y=355)
    l4=Label(master=window,text="PROCESS 4 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l4.place(x=20,y=455)
    l5=Label(master=window,text="PROCESS 5 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l5.place(x=20,y=555)
    w1=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w1.place(x=375,y=155)
    w2=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w2.place(x=375,y=255)
    w3=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w3.place(x=375,y=355)
    w4=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w4.place(x=375,y=455)
    w5=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w5.place(x=375,y=555)
    t1=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t1.place(x=575,y=155)
    t2=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t2.place(x=575,y=255)
    t3=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t3.place(x=575,y=355)
    t4=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t4.place(x=575,y=455)
    t5=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t5.place(x=575,y=555)
    awt=Label(master=window,text="Average waiting time:",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    awt.place(x=775,y=300)
    awta=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    awta.place(x=1150,y=300)
    tatb=Label(master=window,text="Average turn around time:",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    tatb.place(x=775,y=400)
    tata=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    tata.place(x=1200,y=400)
    total=Button(master=window,text="CALCULATE",bg="white",command=totale,fg="green",font=("helvetica",15,"bold"))
    total.place(x=525,y=650)
    clear=Button(master=window,text="CLEAR",bg="white",command=clear1,fg="red",font=("helvetica",15,"bold"))
    clear.place(x=800,y=650)
def sjfa():
    window=Tk()
    window.geometry("2000x2000")
    window.title("SJF")
    window.configure(bg="tomato")
    global e1,e2,e3,e4,e5,y1,y2,y3,y4,y5,l1,l2,l3,l4,l5
    title=Label(master=window,text="SJF",bg="YELLOW",fg="green",font=("helvetica",70,"bold"))
    title.place(x=1000,y=90)

    m0=Label(master=window,text="BRUST TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m0.place(x=20,y=80)

    m1=Label(master=window,text="PROCESSES",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m1.place(x=170,y=80)
    m2=Label(master=window,text="NEW TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m2.place(x=320,y=80)
    m3=Label(master=window,text="WAITING TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m3.place(x=500,y=80)

    m4=Label(master=window,text="TURN AROUND TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m4.place(x=700,y=80)



    e1=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e1.place(x=50,y=155)
    e2=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e2.place(x=50,y=255)
    e3=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e3.place(x=50,y=355)
    e4=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e4.place(x=50,y=455)
    e5=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e5.place(x=50,y=555)
    
    l1=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    l1.place(x=200,y=155)
    l2=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    l2.place(x=200,y=255)
    l3=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    l3.place(x=200,y=355)
    l4=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    l4.place(x=200,y=455)
    l5=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    l5.place(x=200,y=555)

    q1=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    q1.place(x=375,y=155)
    q2=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    q2.place(x=375,y=255)
    q3=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    q3.place(x=375,y=355)
    q4=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    q4.place(x=375,y=455)
    q5=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    q5.place(x=375,y=555)

    w1=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w1.place(x=575,y=155)
    w2=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w2.place(x=575,y=255)
    w3=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w3.place(x=575,y=355)
    w4=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w4.place(x=575,y=455)
    w5=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    w5.place(x=575,y=555)

    t1=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t1.place(x=775,y=155)
    t2=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t2.place(x=775,y=255)
    t3=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t3.place(x=775,y=355)
    t4=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t4.place(x=775,y=455)
    t5=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t5.place(x=775,y=555)

    awt=Label(master=window,text="Average waiting time:",bg="tomato",fg="green",font=("helvetica",20,"bold"))
    awt.place(x=890,y=300)
    awta=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",20,"bold"))
    awta.place(x=1190,y=300)
    tatb=Label(master=window,text="Average turn around time:",bg="tomato",fg="green",font=("helvetica",20,"bold"))
    tatb.place(x=890,y=400)
    tata=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",20,"bold"))
    tata.place(x=1250,y=400)
    total=Button(master=window,text="CALCULATE",bg="white",command=totale1,fg="green",font=("helvetica",15,"bold"))
    total.place(x=525,y=650)
    clear=Button(master=window,text="CLEAR",bg="white",command=clear1,fg="red",font=("helvetica",15,"bold"))
    clear.place(x=800,y=650)
def pri():
    window=Tk()
    window.geometry("1450x800")
    window.title("Priority")
    window.configure(bg="tomato")
    m0=Label(master=window,text="PRIORITY",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m0.place(x=150,y=80)
    title=Label(master=window,text="PRIORITY",bg="YELLOW",fg="green",font=("helvetica",40,"bold"))
    title.place(x=1000,y=90)
    m1=Label(master=window,text="BURST TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m1.place(x=320,y=80)
    m2=Label(master=window,text="WAITING TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m2.place(x=500,y=80)
    m3=Label(master=window,text="TURN AROUND TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    m3.place(x=700,y=80)

    e1=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e1.place(x=175,y=155)
    e2=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e2.place(x=175,y=255)
    e3=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e3.place(x=175,y=355)
    e4=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e4.place(x=175,y=455)
    e5=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    e5.place(x=175,y=555)

    s1=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    s1.place(x=375,y=155)
    s2=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    s2.place(x=375,y=255)
    s3=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    s3.place(x=375,y=355)
    s4=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    s4.place(x=375,y=455)
    s5=Entry(master=window,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
    s5.place(x=375,y=555)

    l1=Label(master=window,text="PROCESS 1 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l1.place(x=20,y=155)
    l2=Label(master=window,text="PROCESS 2 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l2.place(x=20,y=255)
    l3=Label(master=window,text="PROCESS 3 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l3.place(x=20,y=355)
    l4=Label(master=window,text="PROCESS 4 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l4.place(x=20,y=455)
    l5=Label(master=window,text="PROCESS 5 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    l5.place(x=20,y=555)

    

    t1=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t1.place(x=575,y=155)
    t2=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t2.place(x=575,y=255)
    t3=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t3.place(x=575,y=355)
    t4=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t4.place(x=575,y=455)
    t5=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t5.place(x=575,y=555)

    o1=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o1.place(x=775,y=155)
    o2=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o2.place(x=775,y=255)
    o3=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o3.place(x=775,y=355)
    o4=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o4.place(x=775,y=455)
    o5=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o5.place(x=775,y=555)

    awt=Label(master=window,text="Average waiting time:",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    awt.place(x=975,y=300)
    awta=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    awta.place(x=1180,y=300)
    tatb=Label(master=window,text="Average turn around time:",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    tatb.place(x=975,y=400)
    tata=Label(master=window,text="0",bg="tomato",fg="green",font=("helvetica",15,"bold"))
    tata.place(x=1230,y=400)
    total=Button(master=window,text="CALCULATE",bg="white",command=totale2,fg="green",font=("helvetica",15,"bold"))
    total.place(x=525,y=650)
    
def start():
    btnstart.destroy()
    labelimage.destroy()
    fcfsa()
   

    
def fcfsa():

    fcfs = Button(root, text = 'FCFS',relief = FLAT,
    border = 0,font=("helvetica",40,"bold"),command = fcfsb )
    fcfs.place(x =100,y=500)
        
    sjf = Button(root, text = 'SJF',relief = FLAT,
    border = 0,font=("helvetica",40,"bold"),command=sjfa)
    sjf.place(x =440,y=500)

    priority= Button(root, text = 'PRIORITY',relief = FLAT,
    border = 0,font=("helvetica",40,"bold"),command=pri)
    priority.place(x =670,y=500)

    other = Button(root, text = 'other',relief = FLAT,
    border = 0,font=("helvetica",40,"bold"))
    other.place(x =1050,y=500) 

    root.mainloop()
    


img1 = PhotoImage(file="title (1).png")

labelimage = Label(
    root,
    image = img1,
    background = "tomato"
)
labelimage.pack(pady=(40,0))



img2 = PhotoImage(file="Frame.png")
btnstart = Button(root,command = start,image = img2,
    relief = FLAT,
    border = 0,
    background = 'tomato')
btnstart.place(x=575,y=600)




root.mainloop()
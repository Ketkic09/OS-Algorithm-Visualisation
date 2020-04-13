from tkinter import *
from tkinter import messagebox
import tkinter as tk
import os
import random
import time

window=Tk()
window.geometry("1450x800")
window.title("Priority")
window.configure(bg="tomato")
wait=15
global e1,e2,e3,e4,e5,s1,s2,s3,s4,s5,v1,v2,v3,v4,v5,y1,y2,y3,y4,y5
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
    canvas.create_rectangle(700,100,900,400,outline="#fb0",fill="#fb0")
    #RED BALLS FOR BRUST TIME
    ball1=canvas.create_oval(100,300,150,250,fil="red")
    ball2=canvas.create_oval(200,300,250,250,fil="red")
    ball3=canvas.create_oval(300,300,350,250,fil="red")
    ball4=canvas.create_oval(400,300,450,250,fill="red")
    ball5=canvas.create_oval(500,300,550,250,fill="red")
    #TEXT FOR BRUST TIME
    text5=canvas.create_text(525,275,text=v1,font=18)
    text4=canvas.create_text(425,275,text=v2,font=18)
    text3=canvas.create_text(325,275,text=v3,font=18)
    text2=canvas.create_text(225,275,text=v4,font=18)
    text1=canvas.create_text(125,275,text=v5,font=18)
    #GREEN BALLS FOR PRIORITY
    ball6=canvas.create_oval(100,400,150,350,fil="green")
    ball7=canvas.create_oval(200,400,250,350,fil="green")
    ball8=canvas.create_oval(300,400,350,350,fil="green")
    ball9=canvas.create_oval(400,400,450,350,fill="green")
    ball10=canvas.create_oval(500,400,550,350,fill="green")
    #TEXT FOR PRIORITY
    text10=canvas.create_text(525,375,text=y1,font=18)
    text9=canvas.create_text(425,375,text=y2,font=18)
    text8=canvas.create_text(325,375,text=y3,font=18)
    text7=canvas.create_text(225,375,text=y4,font=18)
    text6=canvas.create_text(125,375,text=y5,font=18)
    
    
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







def vis1():
    tk=Tk()
    tk.title("Graphics")

    Height=1000
    Width=1000
    canvas=Canvas(tk,width=Width,height=Height)
    canvas.pack()



    bt1=Button(tk, text="START", width=10, command=ball)
    bt1.place(x=500,y=500)
    


def totale():
    global s1,s2,s3,s4,s5,v1,v2,v3,v4,v5,y1,y2,y3,y4,y5
    n=5
    wt=[]
    tat=[]
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
    #TAKING BRUST VALUES    
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
    bt.append(v4)
    bt.append(v5)
    print(bt)
    #processes=[]
    all=[]
    
    wt.insert(0,0)
    tat = []

    # START FROM HERE
	
    for i in range(n):
        all.append([priority[i],bt[i],i+1])
    all.sort()
    print(all)
    i = 0
    while i!=n-1 :
    	print('while')
    	for i in range(n-1) :
    		if all[i][0] == all[i+1][0]:
    			temp = all[i][1]
    			all[i][1] = all[i+1][1]
    			all[i+1][1]=temp
    	i+=1

    print(all)

    for i in range(1,n):
        wt.append(wt[i-1]+all[i-1][1])
    avgwt = 0     
    for i in range(n):
        avgwt = avgwt + wt[i]
    avgwt = avgwt/n
    for i in range(n):
        tat.append(wt[i]+all[i][1])
    avgtat = 0
    for i in range(n):
        avgtat = avgtat + tat[i]
    avgtat = avgtat/n    
    #TILL HERE
    print(avgwt)
    print(avgtat)
    t1=Label(master=None,text=wt[0],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t1.place(x=575,y=155)
    t2=Label(master=None,text=wt[1],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t2.place(x=575,y=255)
    t3=Label(master=None,text=wt[2],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t3.place(x=575,y=355)
    t4=Label(master=None,text=wt[3],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t4.place(x=575,y=455)
    t5=Label(master=None,text=wt[4],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    t5.place(x=575,y=555)
    o1=Label(master=None,text=tat[0],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o1.place(x=775,y=155)
    o2=Label(master=None,text=tat[1],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o2.place(x=775,y=255)
    o3=Label(master=None,text=tat[2],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o3.place(x=775,y=355)
    o4=Label(master=None,text=tat[3],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o4.place(x=775,y=455)
    o5=Label(master=None,text=tat[4],bg="tomato",fg="green",font=("helvetica",25,"bold"))
    o5.place(x=775,y=555)
    awta=Label(master=None,text=avgwt,bg="tomato",fg="green",font=("helvetica",15,"bold"))
    awta.place(x=1180,y=300)
    tata=Label(master=None,text=avgtat,bg="tomato",fg="green",font=("helvetica",15,"bold"))
    tata.place(x=1230,y=400)
    total=Button(master=None,text="CALCULATE",bg="white",command=totale,fg="green",font=("helvetica",15,"bold"))
    total.place(x=525,y=650)
    vis=Button(master=window,text="VISUALIZATION",bg="white",command=vis1,fg="red",font=("helvetica",15,"bold"))
    vis.place(x=1075,y=650)
    

m0=Label(master=None,text="PRIORITY",bg="tomato",fg="green",font=("helvetica",15,"bold"))
m0.place(x=150,y=80)
title=Label(master=None,text="PRIORITY",bg="YELLOW",fg="green",font=("helvetica",40,"bold"))
title.place(x=1000,y=90)
m1=Label(master=None,text="BURST TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
m1.place(x=320,y=80)
m2=Label(master=None,text="WAITING TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
m2.place(x=500,y=80)
m3=Label(master=None,text="TURN AROUND TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
m3.place(x=700,y=80)
#priority
e1=Entry(master=None,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
e1.place(x=175,y=155)
e2=Entry(master=None,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
e2.place(x=175,y=255)
e3=Entry(master=None,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
e3.place(x=175,y=355)
e4=Entry(master=None,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
e4.place(x=175,y=455)
e5=Entry(master=None,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
e5.place(x=175,y=555)
#BT
s1=Entry(master=None,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
s1.place(x=375,y=155)
s2=Entry(master=None,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
s2.place(x=375,y=255)
s3=Entry(master=None,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
s3.place(x=375,y=355)
s4=Entry(master=None,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
s4.place(x=375,y=455)
s5=Entry(master=None,width=3,font=("Calibri",20),justify='center',relief="solid",bg="white")
s5.place(x=375,y=555)




l1=Label(master=None,text="PROCESS 1 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
l1.place(x=20,y=155)
l2=Label(master=None,text="PROCESS 2 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
l2.place(x=20,y=255)
l3=Label(master=None,text="PROCESS 3 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
l3.place(x=20,y=355)
l4=Label(master=None,text="PROCESS 4 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
l4.place(x=20,y=455)
l5=Label(master=None,text="PROCESS 5 :",bg="tomato",fg="green",font=("helvetica",15,"bold"))
l5.place(x=20,y=555)



t1=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
t1.place(x=575,y=155)
t2=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
t2.place(x=575,y=255)
t3=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
t3.place(x=575,y=355)
t4=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
t4.place(x=575,y=455)
t5=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
t5.place(x=575,y=555)

o1=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
o1.place(x=775,y=155)
o2=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
o2.place(x=775,y=255)
o3=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
o3.place(x=775,y=355)
o4=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
o4.place(x=775,y=455)
o5=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
o5.place(x=775,y=555)

awt=Label(master=None,text="Average waiting time:",bg="tomato",fg="green",font=("helvetica",15,"bold"))
awt.place(x=975,y=300)
awta=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",15,"bold"))
awta.place(x=1180,y=300)
tatb=Label(master=None,text="Average turn around time:",bg="tomato",fg="green",font=("helvetica",15,"bold"))
tatb.place(x=975,y=400)
tata=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",15,"bold"))
tata.place(x=1230,y=400)
total=Button(master=None,text="CALCULATE",bg="white",command=totale,fg="green",font=("helvetica",15,"bold"))
total.place(x=525,y=650)


tk.mainloop()
from tkinter import *
from tkinter import messagebox
import tkinter as tk
window=Tk()
window.geometry("1450x800")
window.title("Priority")
window.configure(bg="tomato")
wait=15
def totale():
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

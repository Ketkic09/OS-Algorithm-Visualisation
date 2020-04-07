from tkinter import *
from tkinter import messagebox
import tkinter as tk

root = Tk()

root.title('OS algorithm visualisation ')
root.geometry('1450x800')
root.configure(bg="tomato")
    
def start():
    btnstart.destroy()
    labelimage.destroy()
   

    
    def fcfsa():

        
        window=Tk()
        window.geometry("1450x800")
        window.title("FCFS")
        window.configure(bg="tomato")
        wait=15
        global e1,e2,e3,e4,e5,y1,y2,y3,y4,y5
        def totale():
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
            w1=Label(master=None,text=wt[0],bg="tomato",fg="green",font=("helvetica",25,"bold"))
            w1.place(x=375,y=155)
            w2=Label(master=None,text=wt[1],bg="tomato",fg="green",font=("helvetica",25,"bold"))
            w2.place(x=375,y=255)
            w3=Label(master=None,text=wt[2],bg="tomato",fg="green",font=("helvetica",25,"bold"))
            w3.place(x=375,y=355)
            w4=Label(master=None,text=wt[3],bg="tomato",fg="green",font=("helvetica",25,"bold"))
            w4.place(x=375,y=455)
            w5=Label(master=None,text=wt[4],bg="tomato",fg="green",font=("helvetica",25,"bold"))
            w5.place(x=375,y=555)
            t1=Label(master=None,text=tat[0],bg="tomato",fg="green",font=("helvetica",25,"bold"))
            t1.place(x=575,y=155)
            t2=Label(master=None,text=tat[1],bg="tomato",fg="green",font=("helvetica",25,"bold"))
            t2.place(x=575,y=255)
            t3=Label(master=None,text=tat[2],bg="tomato",fg="green",font=("helvetica",25,"bold"))
            t3.place(x=575,y=355)
            t4=Label(master=None,text=tat[3],bg="tomato",fg="green",font=("helvetica",25,"bold"))
            t4.place(x=575,y=455)
            t5=Label(master=None,text=tat[4],bg="tomato",fg="green",font=("helvetica",25,"bold"))
            t5.place(x=575,y=555)
            awt=Label(master=None,text="Average waiting time:",bg="tomato",fg="green",font=("helvetica",25,"bold"))
            awt.place(x=775,y=300)
            awta=Label(master=None,text=avgwt,bg="tomato",fg="green",font=("helvetica",25,"bold"))
            awta.place(x=1150,y=300)
            tatb=Label(master=None,text="Average turn around time:",bg="tomato",fg="green",font=("helvetica",25,"bold"))
            tatb.place(x=775,y=400)
            tata=Label(master=None,text=avgtat,bg="tomato",fg="green",font=("helvetica",25,"bold"))
            tata.place(x=1200,y=400)
            total=Button(master=None,text="CALCULATE",bg="white",command=totale,fg="green",font=("helvetica",15,"bold"))
            total.place(x=525,y=650)

        title=Label(master=None,text="FCFS",bg="YELLOW",fg="green",font=("helvetica",70,"bold"))
        title.place(x=900,y=90)
        m1=Label(master=None,text="BURST TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
        m1.place(x=130,y=80)
        m2=Label(master=None,text="WAITING TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
        m2.place(x=320,y=80)
        m3=Label(master=None,text="TURN AROUND TIME",bg="tomato",fg="green",font=("helvetica",15,"bold"))
        m3.place(x=500,y=80)
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
        w1=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
        w1.place(x=375,y=155)
        w2=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
        w2.place(x=375,y=255)
        w3=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
        w3.place(x=375,y=355)
        w4=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
        w4.place(x=375,y=455)
        w5=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
        w5.place(x=375,y=555)
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
        awt=Label(master=None,text="Average waiting time:",bg="tomato",fg="green",font=("helvetica",25,"bold"))
        awt.place(x=775,y=300)
        awta=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
        awta.place(x=1150,y=300)
        tatb=Label(master=None,text="Average turn around time:",bg="tomato",fg="green",font=("helvetica",25,"bold"))
        tatb.place(x=775,y=400)
        tata=Label(master=None,text="0",bg="tomato",fg="green",font=("helvetica",25,"bold"))
        tata.place(x=1200,y=400)
        total=Button(master=None,text="CALCULATE",bg="white",command=totale,fg="green",font=("helvetica",15,"bold"))
        total.place(x=525,y=650) 
            
        
   

    fcfs = Button(root, text = 'FCFS',relief = FLAT,
    border = 0,font=("helvetica",40,"bold"),command = fcfsa )
    fcfs.place(x =100,y=500)
        
    sjf = Button(root, text = 'SJF',relief = FLAT,
    border = 0,font=("helvetica",40,"bold"))
    sjf.place(x =440,y=500)

    priority= Button(root, text = 'PRIORITY',relief = FLAT,
    border = 0,font=("helvetica",40,"bold"))
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
btnstart.place(x=575,y=700)




root.mainloop()
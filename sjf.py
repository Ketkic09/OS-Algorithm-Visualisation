n=int(input("enter number of process = "))
bt=[]
p=[]
for i in range(0,n):
    p.insert(i,i+1)
print("enter brust time")
for i in range(0,n):
    a=int(input())
    bt.append(a)

for i in range(0,n-1):
    for j in range(0,n-i-1):
        if(bt[j]>bt[j+1]):
           temp=bt[j]
           bt[j]=bt[j+1]
           bt[j+1]=temp
           temp=p[j]
           p[j]=p[j+1]
           p[j+1]=temp
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
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0,n):
 print(str(p[i])+"\t\t"+str(bt[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
 print("\n")
print("Average Waiting time is = "+str(avgwt))
print("Average Turn Arount Time is = "+str(avgtat))   

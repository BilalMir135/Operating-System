#Round Robin CPU Scheduling Algorithm
import numpy as np
import pandas as pd
from tabulate import tabulate

Processes=[]
num_of_processes = int(input('Enter number of processes = '))
for x in range(num_of_processes):
    Processes.append([x,'p'+str(x),x,int(input('Enter number of instructions for p'+str(x)+' = ')),0])
BT = [x[3] for x in Processes]

QN = int(input('Enter Quantum Number = '))

total_time =0
RQ = []
count=1
for x in range(len(Processes)):
    total_time += Processes[x][3] 
    
def ready_queue(arrival_time):
    if(arrival_time<=len(Processes)-1):
        for x in range(len(Processes)):
            if(Processes[x][2]==arrival_time):
                RQ.append(Processes[x])
                
ready_queue(count-1)
while(count<=total_time):
    if(len(RQ)!=0):
        p = RQ.pop(0)
        if(p[3]>0):
            if(p[3]-QN>0):
                print(f'{p[1]} => {QN} instructions were executed => {p[3]-QN} instructions are remaining')
                p[3] = p[3]-QN
                c = QN           
            elif(p[3]-QN==0 ):
                print(f'{p[1]} => {QN} instructions were executed => Task finished')
                p[3] = 0
                c = QN
                p[4] = count+QN-1
            elif(p[3]-QN<0):
                print(f'{p[1]} => {p[3]} instruction was executed => Task finished')
                c = p[3]
                p[3]=0
                p[4] = count
        for x in range(c):
            ready_queue(count)
            count +=1
        if(p[3]>0):
            RQ.append(p)

tabel = {
    'Process ID' :[x[0] for x in Processes],
    'Process Name':[x[1] for x in Processes],
    'Arrival Time':[x[2] for x in Processes],
    'Execution Time':BT,
    'Exit Time': [x[4] for x in Processes],
}
tabel['Turn Around Time'] = [x-y for x,y in zip(tabel['Exit Time'],tabel['Arrival Time'])]
tabel['Wait Time'] = [x-y for x,y in zip(tabel['Turn Around Time'],tabel['Execution Time'])]
tabel['Utilization']=[str(round((x/y)*100,2))+'%' for x,y in zip(tabel['Execution Time'],tabel['Turn Around Time'])]
df = pd.DataFrame(tabel)

print(tabulate(df,headers=df.columns,showindex=False,tablefmt='fancy_grid'))
print('Average Turn Around Time = ',round(np.average(tabel['Turn Around Time']),2))
print('Average Wait Time        = ',round(np.average(tabel['Wait Time']),2))

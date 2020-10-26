
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
colors = (0,0,0)
area = np.pi*3
l=[]

AA={'A':[],'R':[],'N':[],'D':[],
'C':[],'E':[],'Q':[],'G':[],
'H':[],'O':[],'I':[],'L':[],'K':[],
'M':[],'F':[],'P':[],'U':[],
'S':[],'T':[],'W':[],'Y':[],'V':[],'unknown':[]}

Score,t=[],0
for filename in os.listdir("sampleCSV"):
    t+=1
    with open(os.path.join("sampleCSV/")+filename,'rt')as f:
        data = csv.reader(f)
        s=0
        if(filename!='unknown.csv'):
            with open(os.path.join("AA-EnergyContents/")+filename.replace('.csv','')+"-EContent.csv",'rt') as f2:
                data2=csv.reader(f2)
                header=next(data)
                header2=next(data2)
                list_data2=list(data2)
                print('%s  : %s' %(t,filename))

                

                for row in data:
                    phi,psi=float(row[0]),float(row[1])
                    xE,yE=0,0
                    phi=0 if(phi==360) else phi
                    psi=0 if(psi==360) else psi
                    m=phi//18
                    n=psi//18
                    xE=int(m+9) if m>=0 else int(m+10)
                    yE=int(m+9) if n>=0 else int(n+10)


                    E=list_data2[xE][yE]
                    if(E=='inf'): E='0'
                    s+=float(E)

                Score.append(s)
                print(s)
print('final score :%s'% sum(Score))


            

            
            

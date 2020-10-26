
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
for item in AA.items():
    with open(item[0]+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['PHI','PSI'])
m=0

for filename in os.listdir("csvdata-7000"):
    m+=1
    with open(os.path.join("csvdata-7000/")+filename,'rt')as f:
            data = csv.reader(f)
            header=next(data)
            print('%s  : %s' %(m,filename))
            rows=[]
            for row in data:
                residue= row[2]
                phi,psi= row[14],row[15]
                if residue!='!*':
                    #chain border
                    if not residue in AA:
                        residue='unknown'
                        AA[residue].append((row[2],phi, psi))
                    else:
                        AA[residue].append((phi, psi))


for item in AA.items():
    with open(item[0]+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['PHI','PSI'])
        if item[0]=='unknown':
            for tpl in item[1]:
                writer.writerow([tpl[0],tpl[1],tpl[2]])
        else:
            for tpl in item[1]:
                writer.writerow([tpl[0],tpl[1]])

            #plt.scatter(phi, psi, s=area, c=colors, alpha=0.5)

            

            
            

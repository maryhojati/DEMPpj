#step 4: Parsing all .dssp files and puting their data in csv file
#next step: plotting data
from collections import OrderedDict
import csv
import os

dic=OrderedDict()
dic={'#':5,'RESIDUE':7,'AA':3 ,'STRUCTURE':10, 'BP1':4, 'BP2':4,'ACC':5,'N-H-->O 1':12,
'O-->H-N 1':11,'N-H-->O 2':11,'O-->H-N 2':11,'TCO':8,'KAPPA':6,'ALPHA':6,'PHI':6,'PSI':6,'X-CA':7,
'Y-CA':7,'Z-CA':7}
#ther={'CHAIN':17, 'AUTHCHAIN':10,'NUMBER':11,'RESNUM':11,'BP1':11,'BP2':11,'N-H-->O':11,
#'O-->H-N':11,'N-H-->O':11,'O-->H-N':11}
for filename in os.listdir("tstdssp"):
    with open(os.path.join('tstdssp', filename), 'r') as f:
        try:
            os.mkdir("./CSV")
        except OSError as e:
            print("Directory exists")

        with open('./CSV/'+filename.replace('dssp','csv'), 'w', newline='') as file:
            print('parsing %s...'%filename)
            writer = csv.writer(file)
            writer.writerow(list(dic.keys()))
            t=c=0
            try:
                for line in f:
                    if(len(line)>2):
                        if('#' in line[1:6]):
                            t=1
                            c+=1
                            continue
                        if(t==1):
                            lst=[]
                            idxEnd=0
                            for key in dic.keys():
                                idxstart=idxEnd
                                idxEnd+=dic[key]
                                lst+=[line[idxstart:idxEnd].strip()]
                            
                            writer.writerow(lst)

            except:
                print("An exception occurred in parsing %s ."%filename)

#
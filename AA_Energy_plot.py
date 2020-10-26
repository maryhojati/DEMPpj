from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
sum = np.zeros([18, 18],dtype=int)
print(138//10)


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import os
AA={'A':'Alanine','R':'Arginine','N':'Asparagine','D':'Aspartic acid',
'C':'Cysteine','E':'Glutamic acid','Q':'Glutamine','G':'Glycine',
'H':'Histidine','O':'Hydroxyproline','I':'Isoleucine','L':'Leucine','K':'Lysine',
'M':'Methionine','F':'Phenylalanine','P':'Proline','U':'Pyroglutamatic',
'S':'Serine','T':'Threonine','W':'Tryptophan','Y':'Tyrosine','V':'Valine','unknown':'Unknown'}
def Energy(frq):
    K=1.380649*(10)**(-23)
    T=273.15
    E=-1*T*np.log10(frq)
    return E
m=0
for filename in os.listdir("AAcsv"):
    m+=1
    data = pd.read_csv("AAcsv/"+filename)
    data['PHI'] = data['PHI'].replace([360],0)
    data['PSI'] = data['PSI'].replace([360],0)
    phi = data['PHI']
    psi=data['PSI']
    #for i in range(len(phi)):
    #    rphi=phi[i]//10
    #    rpsi=psi[i]//10
    #    sum[rphi][rpsi]+=1
    f=plt.figure(m)
    plt.scatter(phi, psi, s=1, alpha=0.02, edgecolor='black', linewidth=1)
    fname=filename.replace('.csv','')
    plt.title(AA[fname])
    plt.xlabel('PHI')
    plt.ylabel('PSI')
    plt.tight_layout()
    #plt.savefig(AA[fname]+'.png')
    hist,xbin,ybin,mi=plt.hist2d(phi, psi, bins=20, cmap=plt.cm.bone_r)
    print(hist)
    print(str(type(hist))+str(type(xbin)))
    with open(fname+'-EContent.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(fname)
        for l in hist:
            eList=[]
            for item in l:
                E=Energy(item)
                eList.append(str(E))
            file.write(','.join(eList))
            file.write('\n')

    #h =plt.hist2d(phi, psi)
    #plt.colorbar(h[3])
    plt.savefig(AA[fname]+'.png')
plt.show()



            
            

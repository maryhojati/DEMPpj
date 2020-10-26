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

m=0
for filename in os.listdir("AAcsv"):
    m+=1
    data = pd.read_csv("AAcsv/"+filename)
    data['PHI'] = data['PHI'].replace([360],0)
    data['PSI'] = data['PSI'].replace([360],0)
    phi = data['PHI']
    psi=data['PSI']
    f=plt.figure(m)
    plt.scatter(phi, psi, s=1, alpha=0.02, edgecolor='black', linewidth=1)
    #plt.scatter(phi, psi, c='black')
    fname=filename.replace('.csv','')
    #plt.title('3q91')
    plt.title(AA[fname])
    plt.xlabel('PHI')
    plt.ylabel('PSI')
    plt.tight_layout()
    plt.savefig(AA[fname]+'.png')
plt.show()



            
            

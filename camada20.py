# import matplotlib.pyplot as plt             
import numpy as np             
from atomlayers import layers         
             
e1, s1, p1, d1 = np.genfromtxt(f'PDOS{layers[19][0]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e2, s2, p2, d2 = np.genfromtxt(f'PDOS{layers[19][1]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e3, s3, p3, d3 = np.genfromtxt(f'PDOS{layers[19][2]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e4, s4, p4, d4 = np.genfromtxt(f'PDOS{layers[19][3]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e5, s5, p5, d5 = np.genfromtxt(f'PDOS{layers[19][4]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e6, s6, p6, d6 = np.genfromtxt(f'PDOS{layers[19][5]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e7, s7, p7, d7 = np.genfromtxt(f'PDOS{layers[19][6]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e8, s8, p8, d8 = np.genfromtxt(f'PDOS{layers[19][7]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
            
dos1 = s1 + p1 + d1             
dos2 = s2 + p2 + d2             
dos3 = s3 + p3 + d3             
dos4 = s4 + p4 + d4             
dos5 = s5 + p5 + d5             
dos6 = s6 + p6 + d6             
dos7 = s7 + p7 + d7             
dos8 = s8 + p8 + d8             
             
doscamada20 = (             
    dos1 +             
    dos2 +             
    dos3 +             
    dos4 +             
    dos5 +             
    dos6 +             
    dos7 +             
    dos8              
)             
             
doscamada20 = doscamada20 / 8             
             
# plt.figure()             
# plt.plot(e1, doscamada20)             
# plt.axhline(y = 0.0025, color = 'r')             
# plt.xlabel('Energy (eV)')             
# plt.ylabel('DOS (A.U.)')             
# plt.show()             
             
            
           
          
         
        
       
      
     
    
   
  
 

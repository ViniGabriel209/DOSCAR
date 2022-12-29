from cgitb import grey            
import numpy as np            
# import matplotlib.pyplot as plt            
from atomlayers import layers         
            
e1, s1, p1, d1 = np.genfromtxt(f'PDOS{layers[0][0]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e2, s2, p2, d2 = np.genfromtxt(f'PDOS{layers[0][1]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e3, s3, p3, d3 = np.genfromtxt(f'PDOS{layers[0][2]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e4, s4, p4, d4 = np.genfromtxt(f'PDOS{layers[0][3]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e5, s5, p5, d5 = np.genfromtxt(f'PDOS{layers[0][4]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e6, s6, p6, d6 = np.genfromtxt(f'PDOS{layers[0][5]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e7, s7, p7, d7 = np.genfromtxt(f'PDOS{layers[0][6]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e8, s8, p8, d8 = np.genfromtxt(f'PDOS{layers[0][7]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e9, s9, p9, d9 = np.genfromtxt(f'PDOS{layers[0][8]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e10, s10, p10, d10 = np.genfromtxt(f'PDOS{layers[0][9]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e11, s11, p11, d11 = np.genfromtxt(f'PDOS{layers[0][10]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e12, s12, p12, d12 = np.genfromtxt(f'PDOS{layers[0][11]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e13, s13, p13, d13 = np.genfromtxt(f'PDOS{layers[0][12]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e14, s14, p14, d14 = np.genfromtxt(f'PDOS{layers[0][13]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e15, s15, p15, d15 = np.genfromtxt(f'PDOS{layers[0][14]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e16, s16, p16, d16 = np.genfromtxt(f'PDOS{layers[0][15]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e17, s17, p17, d17 = np.genfromtxt(f'PDOS{layers[0][16]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e18, s18, p18, d18 = np.genfromtxt(f'PDOS{layers[0][17]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e19, s19, p19, d19 = np.genfromtxt(f'PDOS{layers[0][18]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e20, s20, p20, d20 = np.genfromtxt(f'PDOS{layers[0][19]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e21, s21, p21, d21 = np.genfromtxt(f'PDOS{layers[0][20]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e22, s22, p22, d22 = np.genfromtxt(f'PDOS{layers[0][21]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e23, s23, p23, d23 = np.genfromtxt(f'PDOS{layers[0][22]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e24, s24, p24, d24 = np.genfromtxt(f'PDOS{layers[0][23]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e25, s25, p25, d25 = np.genfromtxt(f'PDOS{layers[0][24]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e26, s26, p26, d26 = np.genfromtxt(f'PDOS{layers[0][25]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC             
e27, s27, p27, d27 = np.genfromtxt(f'PDOS{layers[0][26]}', unpack = True, usecols = (0, 1, 5, 9)) # usecols = (0, 1, 5, 9) Para cálculos com SOC         
         
dos1 = s1 + p1 + d1            
dos2 = s2 + p2 + d2            
dos3 = s3 + p3 + d3            
dos4 = s4 + p4 + d4            
dos5 = s5 + p5 + d5            
dos6 = s6 + p6 + d6            
dos7 = s7 + p7 + d7            
dos8 = s8 + p8 + d8            
dos9 = s9 + p9 + d9            
dos10 = s10 + p10 + d10            
dos11 = s11 + p11 + d11            
dos12 = s12 + p12 + d12            
dos13 = s13 + p13 + d13            
dos14 = s14 + p14 + d14            
dos15 = s15 + p15 + d15            
dos16 = s16 + p16 + d16            
dos17 = s17 + p17 + d17            
dos18 = s18 + p18 + d18            
dos19 = s19 + p19 + d19            
dos20 = s20 + p20 + d20            
dos21 = s21 + p21 + d21            
dos22 = s22 + p22 + d22            
dos23 = s23 + p23 + d23            
dos24 = s24 + p24 + d24            
dos25 = s25 + p25 + d25            
dos26 = s26 + p26 + d26            
dos27 = s27 + p27 + d27            
            
doscamada1 = (            
    dos1 +            
    dos2 +            
    dos3 +            
    dos4 +            
    dos5 +            
    dos6 +            
    dos7 +            
    dos8 +            
    dos9 +            
    dos10 +            
    dos11 +            
    dos12 +            
    dos13 +            
    dos14 +            
    dos15 +            
    dos16 +            
    dos17 +            
    dos18 +            
    dos19 +            
    dos20 +            
    dos21 +            
    dos22 +            
    dos23 +            
    dos24 +            
    dos25 +            
    dos26 +            
    dos27             
)            
            
doscamada1 = doscamada1/27            
            
# ++++++++++++++++++++++++++++++          
          
# COMMENT FOR THE WHOLE ENERGY ARRAY          
          
# ALSO CHANGE IN plotDOS.py FILE          
n = 2137   # line index of the minimum desired energy value          
          
deleted = np.zeros(n)            
c = 0            
            
for i in range(0, n):            
    deleted[i] = c            
    c = c + 1            
            
deleted = deleted[:].astype(int)            
        #     
e1 = np.delete(e1, deleted)            
          
# ++++++++++++++++++++++++++++++          
            
e1 = np.array([            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1,            
    e1            
])            
            
            
# plt.figure()            
# plt.plot(e1[0], doscamada1)            
# plt.axhline(y = 0.0025, color = 'r')            
# plt.xlabel('Energy (eV)')            
# plt.ylabel('DOS (A.U.)')            
# plt.show()            
        #     
# print(len(e1[0]))            
# print(len(doscamada1))            
           
          
         
        
       
      
     
    
   
  
 

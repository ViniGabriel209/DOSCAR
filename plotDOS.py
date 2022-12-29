from locale import normalize
from termios import VMIN
import numpy as np
from cgitb import grey
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as colors
from camada1 import doscamada1, e1
from camada2 import doscamada2
from camada3 import doscamada3
from camada4 import doscamada4
from camada5 import doscamada5
from camada6 import doscamada6
from camada7 import doscamada7
from camada8 import doscamada8
from camada9 import doscamada9
from camada10 import doscamada10
from camada11 import doscamada11
from camada12 import doscamada12
from camada13 import doscamada13
from camada14 import doscamada14
from camada15 import doscamada15
from camada16 import doscamada16
from camada17 import doscamada17
from camada18 import doscamada18
from camada19 import doscamada19
from camada20 import doscamada20
from camada21 import doscamada21
from camada22 import doscamada22

# ALSO CHANGE IN camada1.py FILE
n = 2137   # line index of the minimum desired energy value

deleted = np.zeros(n)
c = 0

for i in range(0, n):
    deleted[i] = c
    c = c + 1

deleted = deleted[:].astype(int)

doscamada1 = np.delete(doscamada1, deleted)
doscamada2 = np.delete(doscamada2, deleted)
doscamada3 = np.delete(doscamada3, deleted)
doscamada4 = np.delete(doscamada4, deleted)
doscamada5 = np.delete(doscamada5, deleted)
doscamada6 = np.delete(doscamada6, deleted)
doscamada7 = np.delete(doscamada7, deleted)
doscamada8 = np.delete(doscamada8, deleted)
doscamada9 = np.delete(doscamada9, deleted)
doscamada10 = np.delete(doscamada10, deleted)
doscamada11 = np.delete(doscamada11, deleted)
doscamada12 = np.delete(doscamada12, deleted)
doscamada13 = np.delete(doscamada13, deleted)
doscamada14 = np.delete(doscamada14, deleted)
doscamada15 = np.delete(doscamada15, deleted)
doscamada16 = np.delete(doscamada16, deleted)
doscamada17 = np.delete(doscamada17, deleted)
doscamada18 = np.delete(doscamada18, deleted)
doscamada19 = np.delete(doscamada19, deleted)
doscamada20 = np.delete(doscamada20, deleted)
doscamada21 = np.delete(doscamada21, deleted)
doscamada22 = np.delete(doscamada22, deleted)

dos = np.array([
    doscamada1, 
    doscamada2, 
    doscamada3, 
    doscamada4, 
    doscamada5, 
    doscamada6, 
    doscamada7, 
    doscamada8,
    doscamada9,
    doscamada10,
    doscamada11,
    doscamada12,
    doscamada13,
    doscamada14,
    doscamada15,
    doscamada16,
    doscamada17,
    doscamada18,
    doscamada19,
    doscamada20,
    doscamada21,
    doscamada22
])

s = (22, doscamada1.size) # N° de camadas, quantidade de energias
c = np.zeros(s)

for a in range(len(doscamada1)):
    for i in range(0, 22):
        c[i][a] = i + 1


def tridimensionalplot():

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.set_xlabel('Energy (eV)')    
    ax.set_ylabel('Layer')
    ax.set_zlabel('Density of states (A.U.)')

    surf = ax.plot_surface(e1, c, dos, cmap = 'viridis', linewidth = 0, antialiased = False)
    cbar = fig.colorbar(surf, shrink = 0.5, aspect = 5)

    plt.show()


def bidimensionalplot():
    
    ax = plt.subplot()
    # im = ax.pcolormesh(c, e1, dos, cmap = 'viridis')
    im = ax.pcolormesh(c, e1, dos, cmap = 'turbo')
    cbar = plt.colorbar(im, ticks = [dos.min(), dos.max()])
    cbar.ax.set_yticklabels(['min', 'max'])
    cbar.set_label('Density of states (A.U.)')
    plt.xlabel('Energy (eV)')
    plt.ylabel('Layer')
    plt.show()


# tridimensionalplot()
bidimensionalplot()


# This file contains the atomic positions of CsSnI3-TiO2 heterostructure

poscar = open('POSCAR', 'r')
positions = poscar.read().split('\n')
positions = positions[8 : -1]

layers = []

z = [0.000000, 
     1.483500,
     2.967000,
     4.450500, 
     5.934000, 
     7.417500, 
     8.901000, 
     10.384500, 
     11.868000, 
     13.351500, 
     14.835000, 
     17.000000,
     20.054000, 
     23.108000, 
     26.162000, 
     29.216000, 
     32.270000,
     35.323999, 
     38.377999,  
     41.431999,
     44.485999,
     47.539999
     ]

coordinates = []

for i in range(len(positions)):
     coordinates.append(positions[i].split())


for i in range(len(z)):

     atoms = []

     for c in range(len(coordinates)):

          if float(coordinates[c][2]) == z[i]:
               atoms.append(c + 1)
             
     layers.append(atoms)


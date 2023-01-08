Files used to plot a 3D visualization of Projected Density of States for a heterostructure of semiconductors.

It is required the POSCAR file of the unrelaxed heterostructure (used on atomlayers.py file) and the DOSCAR file with a specific amount of points. First run criaFilePerAtom.py file and use plotDOS.py for plotting a 3D or colormap for visualization. If all 'camadas' files plot a DOS graphic, running the pre-plotDOS.py is required before former visualization.

offset.py file is used to plot the band alignment between tha layers. It will read the values present on bandedges.txt file (not present in this repository). These values should be determined from the visualization of bandedges using the camadas files (use ple-plotDOS.py to comment/descomment the matplotlib commands lines).

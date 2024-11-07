# Lattice-Distortion

This repository contains relevant code and data for "Mining lattice distortion, strength, and intrinsic ductility of refractory high-entropy alloys using physics-informed statistical learning" by Christopher Tandoc, Yong-Jie Hu, Liang Qi, and Peter K. Liaw. 
https://doi.org/10.1038/s41524-023-00993-x
Tandoc, C., Hu, Y. J., Qi, L., & Liaw, P. K. (2023). Mining of lattice distortion, strength, and intrinsic ductility of refractory high entropy alloys. npj Computational Materials, 9(1), 53.

https://www.nature.com/articles/s41524-023-00993-x

RMSAD_tool.py is a linux command line script written in python that takes a chemical composition in the form of a text string and prints the lattice distortion in angstroms. 

example usgage: 
./RMSAD_tool.py Ti0.5V0.5

-This script uses pymatgen (https://pymatgen.org/) to process the input string and is thus a requirement for the script to work. Depending on the version of pymatgen you have installed, lines 3 and 380 may need to be modified (https://matsci.org/t/python-problem-with-pymatgen/35720)
-numpy (https://numpy.org/) is also a dependency
-This tool is currently only able to make predictions for compositions containing Ti,Zr,Hf,V,Nb,Ta,Mo,W,Re,Ru and will return an error if any other elements are present in the input
-B2 and elemental feature data are defined in dictionaries at the beginning of the code

training.ipynb and training_data.csv contains code and data to reproduce the rmsad model training that was performed in the paper
-jupyter notebook is needed to open training.ipynb, dependencies are numpy, pymatgen, matplotlib (https://matplotlib.org/), pandas (https://pandas.pydata.org/), and sklearn(https://scikit-learn.org/stable/)

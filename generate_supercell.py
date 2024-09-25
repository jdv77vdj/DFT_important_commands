from ase import io
from ase.io import read, write
from ase.build.supercells import make_supercell
from ase.visualize import view
from ase.geometry import get_layers
import numpy as np

#Make supercell of NxNx1, where N is an integer
N = 3
M = [[N, 0, 0], [0, N, 0], [0, 0, 1]]
structure = io.read('CONTCAR-rx3.vasp')
sc=make_supercell(structure, M)
#sc.center(vacuum=10, axis=2)
view(sc)
#write('supercell.vasp', sc, vasp5=True, sort=True, direct=False)
write('supercell.poscar', sc, sort=True, direct=False)

# Convert conventional cell to primitive cell

from pymatgen.core import Lattice, Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer 
import pymatgen.io.vasp
structure = Structure.from_file("Silicon.vasp")
sga = SpacegroupAnalyzer(structure)
primitive_cell = sga.find_primitive()

# In [path] specify path to where the file is going to be created

pymatgen.io.vasp.Poscar.write_file(pymatgen.io.vasp.Poscar(primitive_cell),'[path]/silicon_primitive.POSCAR')

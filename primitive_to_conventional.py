# Primitive cell to conventional cell

from pymatgen.core import Lattice, Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import pymatgen.io.vasp
structure = Structure.from_file("POSCAR") #Here could specify a path, but POSCAR is in same directory as this script. 
sga = SpacegroupAnalyzer(structure)
sga.get_conventional_standard_structure()
conventional_structure = sga.get_conventional_standard_structure()

# Write file
# In [path], insert path to write the POSCAR file of conventional cell
pymatgen.io.vasp.Poscar.write_file(pymatgen.io.vasp.Poscar(
conventional_structure),’[path]/conventional_cell.POSCAR’)



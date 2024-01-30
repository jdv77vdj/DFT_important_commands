#Script to generate a KPOINTS file automatically give the POSCAR file and a grid density.
from pymatgen.core import Structure
from pymatgen.io.vasp.inputs import Kpoints

# Read the structure from the POSCAR file
structure = Structure.from_file("POSCAR")
Kpoints.automatic_density(structure,kppa=1000)

#kppa is the grid density

# For understanding the documentation, read: https://pymatgen.org/pymatgen.io.vasp.html

#Script to generate a KPOINTS file automatically give the POSCAR file and a grid density.
from pymatgen.core import Structure
from pymatgen.io.vasp.inputs import Kpoints

# Read the structure from the POSCAR file
structure = Structure.from_file("POSCAR")
kpoints = Kpoints.automatic_density(structure,kppa=1000)
#kppa is the grid density
kpoints.write_file("KPOINTS")

# For understanding the meaning of commands and variables, read: https://pymatgen.org/pymatgen.io.vasp.html

import sys
from pymatgen.core import Lattice, Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer 
import pymatgen.io.vasp

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python lattice_parameters.py name_of_file(CONTCAR, POSCAR, etc)")
    sys.exit(1)

file_name = sys.argv[1] 
try:
    structure = Structure.from_file(file_name)
except Exception as e:
    print("Error:", e)
    sys.exit(1)

structure = Structure.from_file("CONTCAR")
sga = SpacegroupAnalyzer(structure)

# Print space group information
gp = sga.get_space_group_number()
gs = sga.get_space_group_symbol()
cs = sga.get_crystal_system()
lt = sga.get_lattice_type()

print(f"Space group number: {gp}\nSpace group symbol: {gs}\nCrystal system: {cs}\nLattice type: {lt}")


conv = sga.get_conventional_standard_structure()
print(conv) # This line prints the lattice parameters + angles + all the positions of the atoms. 

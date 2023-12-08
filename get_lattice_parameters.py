from pymatgen.core import Lattice, Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer 
import pymatgen.io.vasp

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

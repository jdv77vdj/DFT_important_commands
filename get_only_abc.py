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

#structure = Structure.from_file("CONTCAR")
sga = SpacegroupAnalyzer(structure)

conv = sga.get_conventional_standard_structure()
v = conv.lattice.abc;
print(v[0],v[1],v[2]) # prints just one line of vectors

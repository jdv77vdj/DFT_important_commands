# Get the band gap of a DOS calculation with VASP
#EIGENVAL file is needed.

import pymatgen.io.vasp.outputs as pmg
eig = pmg.Eigenval('EIGENVAL')
print('Band gap: ', eig.eigenvalue_band_properties[0])

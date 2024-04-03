#!/bin/bash

# Extraction of lattice parameters for various CONTCARs
# get_only_abc.py file is needed.
for p in {0..10}; do
    python get_only_abc.py CONTCAR-rx2-$p > lp
    cat >> lattice_parameters.dat <<EOF
$p $(<lp)
EOF
done

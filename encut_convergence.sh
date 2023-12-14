#!/bin/bash

### Enter slurm commands here
###
###


vasp=/home/SOFTWARE/vasp_test/vasp_std


for ecut in 300 400 450 500 550 600; do

cat > INCAR<<!
SYSTEM = Si

ISIF = 3
ISTART = 0
ICHARG = 2

ENCUT = $ecut

ISMEAR = 0
SIGMA = 0.1
!

mpirun $vasp > result.vasp

awk '/energy  without entropy=/ {ene=$7; print ene} ' OUTCAR > tmp
tail -2 OSZICAR | awk '/RMM/ {x=$2; print x} ' > tmp2

echo $ecut $( cat tmp ) $( cat tmp2) >> encut.dat

mv EIGENVAL EIGENVAL-$ecut
mv OUTCAR OUTCAR-$ecut
mv OSZICAR OSZICAR-$ecut
rm tmp* CHG*

done

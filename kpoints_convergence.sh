#!/bin/bash

#Input here slurm commands
###
###
###

vasp=/home/SOFTWARE/vasp_test/vasp_std


for k in  5 7 9 11; do

cat >KPOINTS <<!
Automatically generated k-points
 0
Monkhorst-pack
 $k $k $k
 0  0  0
!

mpirun $vasp > result.vasp

awk '/energy  without entropy=/ {ene=$7; print ene} ' OUTCAR > tmp
tail -2 OSZICAR | awk '/RMM/ {x=$2; print x} ' > tmp2

echo $k $( cat tmp ) $( cat tmp2) >> kp.dat

done

#!/bin/bash

#This file is for printing only the first lines of 'get_lattice_parameters.py' without all the atoms positions
output=$(python get_lattice_parameters.py)
# Print the first 9 lines of the output
echo "$output" | head -n 9

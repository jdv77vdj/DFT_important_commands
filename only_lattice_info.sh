#!/bin/bash

#This file is for printing only the first lines of  without all the atoms positions
output=$(python lattice_parameters.py)
# Print the first 9 lines of the output
echo "$output" | head -n 9

#!/bin/bash

# This file prints output of 
output=$(python lattice_parameters.py)
# Print the first 9 lines of the output
echo "$output" | head -n 9

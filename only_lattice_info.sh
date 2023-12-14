#!/bin/bash
# Run the Python script with the provided argument and capture its output
output=$(python get_lattice_parameters.py "$1")
# Print the first 5 lines of the output
echo "$output" | head -n 9

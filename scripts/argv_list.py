# argv_list.py ----

# Print command-line arguments

# Setup ----
import sys

# Print arguments
print(f'Command-line arguments: {sys.argv}')

# Notes on using sys.argv-- stands for system argument values ----
# Any command-line arguments are passed into a list, sys.argv, that can be accessed by the Python program
# The first argument (i.e., sys.argv[0]) is the name of the program

# Print additional information-- include argument list, not the name of the program
num_args = len(sys.argv)
print(f'There are {num_args} command-line arguments: {sys.argv[1:]}')
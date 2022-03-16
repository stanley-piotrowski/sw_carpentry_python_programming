# my_ls.py ----

# Python implementation of the Unix 'ls' function
# Parses argument from the command-line and prints all files with the same suffix (e.g., py)

# Setup ----
import sys
import glob2

# Assertions ----
assert len(sys.argv) == 2, 'One argument required to match suffix'
suffix = sys.argv[1]

# List files ----
glob_pattern = '*' + str(suffix)
filenames = glob2.glob(glob_pattern)
for file in filenames:
    print(file)



# count_stdin.py ----

# Parse data from standard input if none are given

# Setup ----
import sys

# Count the number of lines in a file passed from standard input
count = 0
for line in sys.stdin:
    count += 1

print(f'Number of lines: {count}')

# Test the script with the following code typed at the command-line
# cat <data-file> | python3 scripts/count_stdin.py
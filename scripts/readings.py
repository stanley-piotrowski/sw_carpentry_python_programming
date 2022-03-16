# readings.py ----

# Parse a file from the command-line and print the per-patient mean inflammation

# Setup ----
import sys
import numpy

# Define main function ----
def main():
    script = sys.argv[0] # get the name of the script
    action = sys.argv[1] # use for command-line flags
    filename = sys.argv[2] # grab the file name to be used for loading data

    # Assertion for supported command-line flag operations
    assert action in ['--min', '--max', '--mean'], \
        print(f'Action is not one of --min, --max, --mean: {action}')

    # Load data
    data = numpy.loadtxt(fname=filename, delimiter=',')

    # Match action argument
    if action == '--min':
        values = numpy.min(data, axis=1)
    elif action == '--max':
        values = numpy.max(data, axis=1)
    else:
        values = numpy.mean(data, axis=1)

    # Print for each row
    for val in values:
        print(val)

# Call -- when running Python programs on the command-line, __name__ is always set to __main__
if __name__ == '__main__':
    main() # this would be whatever the function is called (in this case, main)


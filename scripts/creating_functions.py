# creating_functions.py ----
# This script cocuses on creating, debugging, and setting defaults with functions

# Setup ----
import glob2
import numpy
import matplotlib.pyplot

# First function ----

# In general, we want to keep our functions short and to the point-- no more than about 6 lines
# More complex operations can be built up using smaller functions
# Write a function to converts temperature from F to C
def fahr_to_celcius(temp):
    celcius = (temp - 32) * (5/9)
    return(celcius)

# Test
print(f'Freezing point of water: {fahr_to_celcius(32)} C')

# Convert C to K
def celcius_to_kelvin(temp):
    kelvin = temp + 273.15
    return(kelvin)

# Test
print(f'Freezing point of water in Kelvin: {celcius_to_kelvin(0)}')

# Define function to convert F to K
def fahr_to_kelvin(temp):
    temp_c = fahr_to_celcius(temp)
    temp_k = celcius_to_kelvin(temp_c)
    return(temp_k)

# Test
print(f'Boiling point of water in Kelvin: {fahr_to_kelvin(212)}')

# Inflammation analysis ----
# Read data
filenames = glob2.glob('./data/inflammation*.csv')
data = []
for file in filenames:
    data.append(numpy.loadtxt(fname=file, delimiter=','))

# Define function to create summary statistic plots for data set
def plot_summary_stats(input):

    """
    :param input: array
    :return: three subplots with the mean, max, and min across all patients for each day
    """


    fig = matplotlib.pyplot.figure(figsize=(10, 3))

    # Define subplots
    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    # Define what to plot in each
    axes1.plot(numpy.mean(input, axis=0))
    axes2.plot(numpy.max(input, axis=0))
    axes3.plot(numpy.min(input, axis=0))

    # Define y labels
    axes1.set_ylabel('mean')
    axes2.set_ylabel('max')
    axes3.set_ylabel('min')

    # Define layout and plot
    fig.tight_layout()
    # matplotlib.pyplot.show() # comment out for running entire script from the command line

# Create plots for each file
print(f'Creating plots for all inflammation datasets')
for filename in data:
    plot_summary_stats(filename)

# Combining strings ----
# Write a function that takes two parameters-- original and wrapper, and prints the wrapper character at the beginning and end of the original string
def fence(original, wrapper):
    """
    Print the original string encapsulated by the wrapper string.

    Parameters
    ----------
    original: str
    wrapper: str

    Returns
    -------
    out: str

    Examples
    --------
    >>> fence('name', '*')
    *name*

    """
    out = wrapper + original + wrapper
    return(out)

# Test the help documentation
print(f'Printing help documentation')
# help(fence) comment out for testing entire script on the command line

# Test using the example in the exercise
result = fence('name', '*')
print(result)

# Selecting characters from strings ----
# Create a function that takes a string and returns just the first and last characters of its input
def outer(input):
    """
    Return the first and last characters of the input string.

    Parameters
    ----------
    input: str

    Return
    ------
    out: str

    Examples
    --------
    >>> outer('helium')
    hm

    """

    out = input[0] + input[-1]
    return(out)

# Test with the example case
result = outer('helium')
print(result)

# Rescaling an array ----
# Create a function that scales the values in an array to lie between 0 and 1
# The formula for the scaling is (value - L) / (H-L)
def rescale(input_array):
    """
    Rescale all values of an array to lie between 0.0 and 1.0.

    Parameters
    ----------
    input_array: float

    Return
    ------
    out = ndarray

    Examples
    --------


    """
    lowest_val = numpy.min(input_array)
    highest_val = numpy.max(input_array)

    scaling_factors = (input_array - lowest_val) / (highest_val - lowest_val)

    out = scaling_factors * (highest_val - lowest_val) + lowest_val

# Test on the first data set
result = rescale(data[0])


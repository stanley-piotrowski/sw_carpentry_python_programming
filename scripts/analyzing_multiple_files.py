# analyzing_multiple_files.py ----
# Use for loops and different python libraries to analyze data from multiple files

# Setup ----
# Note, the tutorial uses glob, but we'll use glob2
# To install glob2, use the following command
# conda install -c conda-forge glob2
import glob2
import numpy
import matplotlib.pyplot

# Analysis ----
# Grab the file names
filenames = sorted(glob2.glob('./data/inflammation*.csv'))

# Load data
data = []
for filename in filenames:
    data.append(numpy.loadtxt(fname=filename, delimiter=','))

# For each data set, create the three subplots generated earlier showing the mean, max, and min inflammation for each day
for dataset in data:

    fig = matplotlib.pyplot.figure(figsize=(10, 3))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    # Set labels
    axes1.set_ylabel('mean')
    axes2.set_ylabel('max')
    axes3.set_ylabel('min')

    # Plot
    axes1.plot(numpy.mean(dataset, axis=0))
    axes2.plot(numpy.max(dataset, axis=0))
    axes3.plot(numpy.min(dataset, axis=0))

    # Define layout and show plots
    fig.tight_layout()
    matplotlib.pyplot.show()

# Plotting differences ----
# Plot the difference between the average inflammations reported in the first and second datasets
first_two_files = [filenames[0], filenames[1]]
first_two_data = []
for file in first_two_files:
    first_two_data.append(numpy.loadtxt(fname=file, delimiter=','))

# For each data set, calculate the average of each day
means = []
for file in first_two_data:
    means.append(numpy.mean(file, axis=0))

# Create a zip object and use enumerate() in the loop
mean_diffs = []
for i, (mean1, mean2) in enumerate(zip(means[0], means[1])):
    difference = mean2 - mean1
    mean_diffs.append(difference)

# Set y-label and plot
matplotlib.pyplot.ylabel('Difference in mean inflammation')
matplotlib.pyplot.plot(mean_diffs)
matplotlib.pyplot.show()

# Generate composite statistics ----
# Create an array of zeros the same size as each of the csv files
composite_data = numpy.zeroes((60, 40))

# For each file, sum all inflammation measurements for a given day
for dataset in data:
    composite_data += dataset

# Divide by the number of files
composite_data = composite_data / len(filenames)

# Create plots of the average, max, and min for each day
fig = matplotlib.pyplot.figure(figsize=(10, 3))
axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

# Creat subplots
axes1.plot(numpy.mean(composite_data, axis=0))
axes2.plot(numpy.max(composite_data, axis=0))
axes3.plot(numpy.min(composite_data, axis=0))

# Define axis labels
axes1.set_ylabel('mean')
axes2.set_ylabel('max')
axes3.set_ylabel('min')

# Define layout
fig.tight_layout()

# Save plot and view
matplotlib.pyplot.savefig('./figures/summary_stat_plots.png')
matplotlib.pyplot.show()














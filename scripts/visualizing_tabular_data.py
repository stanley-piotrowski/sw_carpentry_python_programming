# visualizing_tabular_data.py ----
# This script focuses on plotting tabular data and generating multiple plots in a single figure
import matplotlib.pyplot
import numpy

# Basic code to create a matplotlib.pyplot heatmap
# The imshow() function shows and image, taking an array-like object as input
data = numpy.loadtxt(fname='./data/inflammation-01.csv', delimiter=',')
image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()

# The plot shows that there are relatively low values of inflammation measurements early on, then after the medication kicks in around 3-weeks after the start of the trial, inflammation starts to decrease again

# We can summarize the mean inflammation measurements for all patients over time
mean_inflammation = numpy.mean(data, axis=0) # compute mean over each day and store as array
mean_plot = matplotlib.pyplot.plot(mean_inflammation)
matplotlib.pyplot.show()

# We can see that the mean inflammation peaks around 20 days, very similar to what we saw in the heatmap

# We can create a composite figure by putting together different subplots using matplotlib.pyplot.figure()
# Define size of plotting area
fig = matplotlib.pyplot.figure(figsize = (10, 3))

# Add subplots-- there is 1 row of plots, 3 columns, and place each side by side
axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

# Define what to plot in each subplot
axes1.plot(numpy.mean(data, axis=0))
axes2.plot(numpy.max(data, axis=0))
axes3.plot(numpy.min(data, axis=0))

# Define axis labels for each subplot
axes1.set_ylabel('mean')
axes2.set_ylabel('max')
axes3.set_ylabel('min')

# Further control layout
fig.tight_layout()

# Save and plot
matplotlib.pyplot.savefig('./figures/inflammation_summaries.png')
matplotlib.pyplot.show()

# Create a plot of the standard deviation of inflammation data
stddev_inflammation = numpy.std(data, axis=0)
stddev_plot = matplotlib.pyplot.plot(stddev_inflammation)
matplotlib.pyplot.savefig('./figures/standard_dev_inflammation.png')
matplotlib.pyplot.show()



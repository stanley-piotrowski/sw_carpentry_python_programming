# intro_analysis.py ----
# Perform introductory analysis using the NumPy module

import numpy

# Import file
file_name = './data/inflammation-01.csv'
data = numpy.loadtxt(fname=file_name, delimiter=',')
print(f'Downloaded {file_name}')

# Get a feel for the data
data_dims = data.shape
print('\nArray dimensions')
print(f'The array has {data_dims[0]} rows and {data_dims[1]} columns')

# Calculate summaries of the data
data_max, data_min, data_std, data_mean = numpy.max(data), numpy.min(data), numpy.std(data), numpy.mean(data)
print('\nSummary statistics')
print(f'Maximum value: {data_max}')
print(f'Minimum value: {data_min}')
print(f'Standard deviation: {data_std}')
print(f'Mean: {data_mean}')

# Calculate mean inflammation for each patient (rows)
print('\nMean inflammation of each patient')
for i in range(0, data_dims[0], 1):
    mean_val = numpy.mean(data[i, :])
    message = f'Mean inflammation of patient {i}: {mean_val}'
    print(message)

# Calculate mean inflammation for each day across patients (columns)
print('\nMean inflammation for each day')
for i in range(0, data_dims[1], 1):
    mean_val = numpy.mean(data[:, i])
    message = f'Mean inflammation on day {i}: {mean_val}'
    print(message)

# We can also calculate the same values using the 'axis' argument in numpy.mean()
print('\nUsing axis argument in numpy.mean()')
print(f'Mean inflammation per patient: {numpy.mean(data, axis=1)}')
print(f'Mean inflammation per day: {numpy.mean(data, axis=0)}')

# Slicing exercises
# To get the last three characters of element, use the following
element = 'oxygen'
last_three = element[-3:]
print(f'Last three elements: {last_three}') # works with 'hi', and 'carpentry' as well

# Slicing the data array
# element[3:3] returns an empty string-- 'starting from the 3rd element, print everything up to but not including the third element'
# data[3:3, 4:4] returns an empty array-- confirmed, shape = (0, 0)
# data[3:3, :] returns an array of 0 rows and 40 columns-- but no data, since we haven't printed any rows

# Stacking arrays
print('\nStacking arrays')
a = numpy.array(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
)

vertical_stack = numpy.vstack([a, a])
horizontal_stack = numpy.hstack([a, a])

print(f'Original array:\n{a}')
print(f'Vertical stack:\n{vertical_stack}')
print(f'Horizontal stack:\n{horizontal_stack}')

# Exercise-- slice the first and last columns of the array and stack them into a 3x2 array
new_array = numpy.hstack((a[:, :1], a[:, -1:]))
print(f'New 3x2 array:\n{new_array}')

# Calculating the difference in inflammation measurements for patients
# numpy.diff() rows, axis == 0; columns, axis == 1
numpy.diff(data, axis=1)

# After running the diff() method, the difference in inflammation measurements for each patient would be 60 rows and 1-number of columns
patient_diff = numpy.diff(data, axis=1)
patient_diff.shape # (60, 39)-- 60 rows and 39 columns

# The difference in days across columns would be 59 rows and 40 columns
time_diff = numpy.diff(data, axis=0)
time_diff.shape # (59, 40)

# In order to find the largest change in inflammation for each patient, we could use numpy.max()
# An increase or decrease matters-- increases indicate higher inflammation relative to the previous measurement
# Decreases indicate lower inflammation relative to the previous measurement
largest_diffs = numpy.max(patient_diff, axis=1)
print(f'Largest patient differences:\n{largest_diffs}')

# If we just want just the magnitude of the change, we can use the abolute() function
absolute_diffs = numpy.absolute(largest_diffs)
print(f'Largest absolute differences:\n{absolute_diffs}')






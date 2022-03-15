# making_choices.py ----
# This script focuses on exploring conditional statements

# Setup ----
import numpy
import glob2

# Load data ----
filenames = glob2.glob('./data/inflammation*.csv')
data = []
for file in filenames:
    data.append(numpy.loadtxt(fname=file, delimiter=','))

# Check for suspicious behavior in the data ----
max_inflammation = []
for dataset in data:
    max_inflammation.append(numpy.max(dataset, axis=0))

# If the maximum inflammation measurements equal the day, flag as suspicious
for data_idx, data in enumerate(max_inflammation):
    print(f'\nWorking on dataset number: {data_idx}')
    for day, measurement in enumerate(data):
        print(f'Day: {day}, max inflammation: {measurement}')
        if day == int(measurement):
            print('SUSPICIOUS MAXIMUM DETECTED')

# We can do something similar with the minimum-- if all of the minimums for a given data set add up to zero, that seems fishy
min_inflammation = []
for dataset in data:
    min_inflammation.append(numpy.min(dataset, axis=0))

for idx, dataset in enumerate(min_inflammation):
    if int(numpy.sum(dataset)) == 0:
        print(f'All minima for dataset {idx} add up to zero!')

# This analysis shows that datasets 1, 7, and 11 are a bit suspicious
# In these particular datasets, the minimum inflammation estimates for all days add up to zero

# Exercise-- how many paths?
# The answer is C because neither of the first two conditions are True, but the last one is

# Exercise -- what is truth?
# After going through the code, the basic rule is that anything with length > 0 is true
# For example, an empty string '' is False; while a string of length 1 ' ' with just a space is True
# Similarly, 0 is False and 1 is True

# Sorting files into buckets ----
# Grab the list of all file names and sort them based on their size
# Note, if the substring doesn't exist in the string, .find() returns -1
all_filenames = glob2.glob('./data/*')
large_files = []
small_files = []

for file in all_filenames:
    if file.find('inflammation') > 0:
        print(f'{file} --> inflammation file directory')
        large_files.append(file)
    elif file.find('small') > 0:
        print(f'{file} --> small file directory')
        small_files.append(file)
    else:
        print(f'{file} --> unknown type directory')

print(f'Number of large files: {len(large_files)}')
print(f'Number of small files: {len(small_files)}')

# Exercise -- counting vowels
# Write a loop that counts the number of vowels in a string
my_string = 'alligator'
vowels = list('aeiou')
total = 0
for vowel in vowels:
    total += my_string.count(vowel)

print(f'Number of vowels in {my_string}: {total}')
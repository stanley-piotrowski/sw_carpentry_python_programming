# loops.py ----
# This script focuses on using loops for iterating over data structures to perform common operations

# Setup
import numpy

# For loops ----
# Basic example of using a for loop
odds = [1, 3, 5, 7, 9, 11]
for num in odds:
    print(num)

# Loops can be used for counting
length = 0
names = ['curie', 'darwin', 'turing']
for name in names:
    length += 1

print(f'There are {length} names in the list.')

# This isn't all that efficient because we could have used the built-in len() function

# Exercise -- from 1 to N
# Use the range() function to write a for loop that prints the first 3 natural numbers
# Use range(1, 4)-- starts at 1 and goes up to, but doesn't include, 4
for num in range(1, 4):
    print(num)

# Exercise -- understanding the loops
# How many times will the loop be executed?
word = 'oxygen'
iterations = 0
for i in range(len(word)):
    print(f'Iteration {i}: {word[i]}')
    iterations += 1

print(f'Total number of iterations: {iterations}') # 6

# Exercise -- write a loop that calculates powers using multiplication
# The exercise is 5 ** 3, which should equal 125
num = 5
power = 3
total = num
for i in range(1, power):
    total *= num

print(num) # 125

# Exercise-- summing a list
# Add each element and print the final value
# E.g. [124, 402, 36] summed together is 562
nums = [124, 402, 36]
total = 0
for num in nums:
    total += num

print(f'Sum of numbers calculated with a loop: {total}')

# You can also use numpy.sum() to do the same computation
print(f'Sums of numbers calculated using numpy: {numpy.sum(nums)}')

# Enumerate -- creates a new sequence pair with the original list and the indexes
# For example, using the nums list
for idx, val in enumerate(nums):
    print(f'Index: {idx}, value: {val}')

# Exercise -- write a solution using loops and enumerate() which computes the value of y at any polynomial given x and coefs
coefs = [2, 4, 3]
x = 5

y = []
for idx, coef in enumerate(coefs):
    y.append(coef * x**idx)

# Print the term and value of y at each polynomial
for idx, val in enumerate(y):
    print(f'Polynomial: {idx + 1}; value of y: {val}')






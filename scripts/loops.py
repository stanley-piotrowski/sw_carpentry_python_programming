# loops.py ----
# This script focuses on using loops for iterating over data structures to perform common operations

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



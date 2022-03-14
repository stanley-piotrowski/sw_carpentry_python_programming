# storing_values_lists.py ----
# This script focuses on using lists to store and manipulate data

# Setup ----
import numpy

# Lists are mutable-- elements can be changed, but that means that two variables that reference the same list in memory will both change
# This is important because there are different functions for modifying lists in place vs functions that modify a copy of the original list
salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
my_salsa = salsa
print(f'Original ingredient list: {salsa}')

# Change the first element
salsa[0] = 'hot peppers'
print(f'New ingredient list: {salsa}')

# Make a copy of the list, then modify the elements
print(f'\nMaking a copy of the list')
salsa = ['peppers', 'onions', 'cilantro', 'tomatoes']
my_salsa = list(salsa)
salsa[0] = 'hot peppers'
print(f'Original ingredient list: {salsa}')
print(f'My ingredient list: {my_salsa}')

# Nested lists ----
print(f'\nCreating a nested list')
nested_foods = [['pepper', 'zucchini', 'onion'],
    ['cabbage', 'lettuce', 'garlic'],
    ['apple', 'pear', 'banana']]

print(nested_foods)

# Print each sublist
print(f'\nPrinting each sublist')
for i in range(0, len(nested_foods)):
    print(f'Element {i}: {nested_foods[i]}')

# Modifying lists ----
# Importantly, the functions below will modify the list in place, without returning any output
salsa.append('salt')
print(f'Adding an ingredient: {salsa}')

last_ingredient = salsa.pop()
print(f'Removing the last ingredient: {salsa}')

salsa.reverse()
print(f'Reversing the list of ingredients: {salsa}')

# Slicing from the end ----
# Slice only the last four characters of a string or entries of a list
# This approach works regardless of the lenght of the string, because the starting position is the 4th last element up to the last
string_for_slicing = 'Observation date: 02-Feb-2013'
list_for_slicing = [['fluorine', 'F'],
                    ['chlorine', 'Cl'],
                    ['bromine', 'Br'],
                    ['iodine', 'I'],
                    ['astatine', 'At']]

# Print original and then sliced
print(f'\nOriginal string: {string_for_slicing}')
print(f'Sliced string: {string_for_slicing[-4:]}')

print(f'\nOriginal list: {list_for_slicing}')
print(f'Sliced list: {list_for_slicing[-4:]}')

# Slicing with step size ----

# Define a list of prime numbers and slice with step size of 3
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
subset = primes[0:12:3]
print(f'Subset of primes with step-size 3: {subset}')

# Exercise-- grab every other character in the string
beatles = "In an octopus's garden in the shade"
print(f'\nOriginal string: {beatles}')
print(f'Every other character: {beatles[0::2]}')

# Operator overloading ---
# Use the addition operator, which will concatenate, and the multiplication operator
counts = [2, 4, 6, 8, 10]
addition_overloading = counts + counts
multiplication_overloading = counts * 2

addition_overloading == multiplication_overloading # returns True

# Both operators return the same output










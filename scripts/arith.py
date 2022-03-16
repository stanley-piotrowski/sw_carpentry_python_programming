# arith.py ----

# This script takes an action (e.g., add, subtract, etc) and two numbers as input, performs the operation, and returns the result

# Setup ----
import sys

# Assertions ----

# Basic input check
assert len(sys.argv) == 4, 'Must pass an action and two numbers as input'

# Check that action is either add, subtract, multiply, or divide
action = sys.argv[1]
assert type(action) == str, 'Action must be a string'
assert action in ['add', 'subtract', 'multiply', 'divide'], 'Invalid action, must be either add, subtract, multiply, or divide: ' + action

# Operation ----

# Convert to float
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])

# Result
if action == 'add':
    result = num1 + num2
elif action == 'subtract':
    result = num1 - num2
elif action == 'multiply':
    result = num1 * num2
else:
    result = num1 / num2

print(result)
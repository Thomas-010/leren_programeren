# test_math_operations.py

from math_operations import increment, decrement, add, subtract, multiply, divide

# Test increment
print("increment(5) =", increment(5))  # Verwacht 6

# Test decrement
print("decrement(5) =", decrement(5))  # Verwacht 4

# Test add
print("add(5, 3) =", add(5, 3))        # Verwacht 8

# Test subtract
print("subtract(5, 3) =", subtract(5, 3))  # Verwacht 2

# Test multiply
print("multiply(5, 3) =", multiply(5, 3))  # Verwacht 15

# Test divide
print("divide(6, 3) =", divide(6, 3))      # Verwacht 2
print("divide(6, 0) =", divide(6, 0))      # Verwacht foutmelding en inf
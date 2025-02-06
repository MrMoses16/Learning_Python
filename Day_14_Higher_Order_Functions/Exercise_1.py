# Explain the difference between map, filter, and reduce.
# Map, filter, and reduce all take in a function and iterable as parameters,
# however, map returns a list of outputs based on the function, filter returns
# a boolean value for each item in the list, and reduce returns one value created
# by the input (iterable) for the function.

# Explain the difference between higher order function, closure and decorator.
# Higher order function take one or more functions as parameters or returns a function.
# Closure allows inner functions to access variables in outer function even after the
# outer function has finished executing. Decorator is a specific type of higher 
# order function that modifies or enhances the behavior of another function

# Define a call function before map, filter and reduce.
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map example:
def cube_num(num):
    return num ** 3
cube_num_list = map(cube_num, numbers)
print(list(cube_num_list))

# Filter example:
def is_odd(num):
    return num & 1 == 1
odd_num_list = filter(is_odd, numbers)
print(list(odd_num_list))

# Reduce example:
def mult_two_num(num1, num2):
    return num1 * num2
mult_list_num = reduce(mult_two_num, numbers)
print(mult_list_num)
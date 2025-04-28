# Function to double a number
def double(x):
    return x * 2
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Use map to double each number in the list
doubled_numbers = map(double, numbers)
# Convert the iterator to a list
doubled_numbers_list = list(doubled_numbers)
print(doubled_numbers_list) # Output: [2, 4, 6, 8, 10]

#Suppose f is a function and [a,b,c] is a list.We want to be able
#to push the function f inside the list and get [f(a),f(b),f(c)].
from math import sin, cos, pi

x = map(sin, range(1, 10))
xlist = list(x)
print(xlist)
#Converting a list of strings to uppercase:
names = ['alice', 'bob', 'charlie']
uppercase_names = map(str.upper, names)
print(list(uppercase_names)) # Output: ['ALICE', 'BOB', 'CHARLIE']
#Calculating the lengths of strings in a list:
words = ['apple', 'banana', 'orange']
lengths = map(len, words)
print(list(lengths)) # Output: [5, 6, 6]
# Rounding off a list of floating-point numbers:
float_numbers = [3.14, 2.718, 1.618]
rounded_numbers = map(round, float_numbers)
print(list(rounded_numbers)) # Output: [3, 3, 2]
#Applying a custom function to a list of tuples:
def product(pair):
    x, y = pair
    return x * y
pairs = [(1, 2), (3, 4), (5, 6)]
products = map(product, pairs)
print(list(products)) # Output: [2, 12, 30]
#Using map() with multiple iterables:
numbers = [1, 2, 3]
squares = [4, 9, 16]
result = map(lambda x, y: x + y, numbers, squares)
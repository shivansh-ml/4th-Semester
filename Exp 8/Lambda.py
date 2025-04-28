lambda x : x**2 + 4
(lambda x : x**2 + 4)(10) # Output is 104
# Giving a name to an anonymous function
f = lambda x: x + 3
print(f(1)) # Output is 4
# Define anonymous functions with several variables
(lambda x, y, z: x + y + z)(1, 2, 3)
(lambda x, y, z: x + y + z)('one', ' two', ' three')
# Define default values for parameters
(lambda x, y, z = 3: x * y * z)(1, 2)
# Checking if a number is even:
is_even = lambda x: x % 2 == 0
print(is_even(6)) # Output: True
print(is_even(7)) # Output: False
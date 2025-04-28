def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

# Using the generator to print even numbers up to 10
for num in even_numbers(10):
    print(num, end=' ') # Output: 0 2 4 6 8
print('\n')

# Generators in Python are special functions that can be paused and resumed.
# They allow you to generate a sequence of values lazily, one at a time, instead
# of computing them all at once and storing them in memory. Generators are
# defined using the yield keyword instead of return. Here’s an example of a
# generator function that generates a sequence of even numbers:

# You can combine map() and generators to apply a function lazily to each item
# of an iterable, avoiding the need to store the entire result in memory. This can
# be particularly useful when dealing with large datasets.

# Generator function to double numbers
def double_generator(numbers):
    for num in numbers:
        yield num * 2
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Using map with the double generator
doubled_numbers = map(double_generator, [numbers])
# Accessing the values using a loop
for nums in doubled_numbers:
    for num in nums:
        print(num, end=' ') # Output: 2 4 6 8 10
# Creating a tuple
t = () # empty tuple
one_element_tuple = (42, ) # you need the comma!
my_tuple = ('apple', 'banana', 'cherry')
print(my_tuple) # Output: ('apple', 'banana', 'cherry')

# Accessing elements from the tuple
print(my_tuple[0]) # Output: 'apple'
print(my_tuple[1]) # Output: 'banana'
print(my_tuple[-1]) # Output: 'cherry'

my_tuple = (1, 2, 3, 2, 4, 2)
count_of_twos = my_tuple.count(2)
print(f"Number of twos in the tuple: {count_of_twos}")
# Output: Number of twos in the tuple: 3
my_tuple = ('apple', 'banana', 'cherry', 'banana')
banana_index = my_tuple.index('banana')
print(f"Index of 'banana': {banana_index}")
# Concatenating two tuples
my_tuple = my_tuple + ('dragonfruit',)
print(my_tuple) # Output: ('apple', 'banana', 'cherry', 'dragonfruit')

# Tuple packing
my_tuple = 1, 2, 3, 'a', 'b', 'c'
# Tuple unpacking
a, b, c, d, e, f = my_tuple
print(a, b, c) # Output: 1 2 3

my_tuple = (1, 2, 3, 'a', 'b', 'c')
for item in my_tuple:
    print(item)

A = [1,2,3]
tuple(A) # output is tuple (1,2,3)
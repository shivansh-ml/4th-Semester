# Creating a set
my_set = {'apple', 'banana', 'cherry'}
print(my_set) # Output: {'apple', 'banana', 'cherry'}
# Empty set
empty_set = set()

my_set = {'apple', 'banana', 'cherry'}
# Check if 'apple' is present in the set
print('apple' in my_set) # Output: True

my_set = {'apple', 'banana', 'cherry'}
# Check if 'apple' is present in the set
print('apple' in my_set) # Output: True

# Adding an item to the set
my_set.add('dragonfruit')
print(my_set) # Output: {'apple', 'banana', 'cherry', dragonfruit'}

# Removing an item from the set
# It raises a key error if element is not present
my_set.remove('banana')
print(my_set) # Output: {'apple', 'cherry', 'dragonfruit'}
# Use of discard which does not raises a error
my_set.discard('banana')
print(my_set) # Output: {'apple', 'cherry', 'dragonfruit'}
# pop(): Removes and returns an arbitrary element from the set.
#Raises a Key Error if the set is empty.
element = my_set.pop()
print(element)
#clear(): Removes all elements from the set, making it empty.
my_set.clear()
print(my_set) # Output: set()
# update(iterable): Adds multiple elements to the set from aniterable.

my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set) # Output: {1, 2, 3, 4, 5, 6}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set) # Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1.intersection(set2)
print(intersection_set) # Output: {3}

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}
difference_set = set1.difference(set2)
print(difference_set) # Output: {1, 2, 5}

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set) # Output: {1, 2, 6, 7}
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 6, 7}


my_set = {1, 2, 3}
superset = {1, 2, 3, 4, 5}
print(my_set.issubset(superset)) # Output: True

# list to a set
list_set = set([1, 2, 3, 4, 5])
# string to set
string_set = set("hello")
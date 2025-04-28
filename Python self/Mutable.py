lst = [1, 2, 3] # lst is a list (mutable)
d = {'a': 1, 'b': 2} # d is a dictionary (mutable)
s = {1, 2, 3} # s is a set (mutable)

lst = [1, 2, 3] # lst is a list (mutable)
d = {'a': 1, 'b': 2} # d is a dictionary (mutable)
s = {1, 2, 3} # s is a set (mutable)

# Mutable objects, on the other hand, can be modified after they are created. When you modify the value of a mutable object,
# the changes are reflected in the original object itself. Mutable objects in Python include: lists, dictionaries, sets, 
# byte arrays, user-defined classes (if they are designed to be mutable)

lst = [1, 2, 3]
lst.append(4) # Modifying the list in place
print(lst) # Output: [1, 2, 3, 4]
d = {'a': 1, 'b': 2}
d['c'] = 3 # Modifying the dictionary in place
print(d) # Output: {'a': 1, 'b': 2, 'c': 3}
s = {1, 2, 3}
s.add(4) # Modifying the set in place
print(s) # Output: {1, 2, 3, 4}
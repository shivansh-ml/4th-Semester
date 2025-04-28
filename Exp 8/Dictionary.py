# Empty dictionary
empty_dict = {}
# Dictionary with key-value pairs
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict) # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Dictionary from key-value pairs using dict() constructor
my_dict = dict(name='John', age=30, city='New York')

# Accessing elements from the dictionary
print(my_dict['name']) # Output: 'John'
#If a key is not present in the dictionary, it raises a Key Error.

#You can also use the get() method to avoid this:
print(my_dict.get('name')) # Output: John
print(my_dict.get('gender', 'N/A')) # Output: N/A (default value)

# keys(): Returns a view object that displays a list of all the keys in the dictionary.
print(my_dict.keys()) # Output: dict_keys(['name', 'age', 'city'])

#values(): Returns a view object that displays a list of all thevalues

#in the dictionary.
print(my_dict.values()) # Output: dict_values(['John', 30, 'NewYork'])

#items(): Returns a view object that displays a list of key-value tuples in the dictionary.
print(my_dict.items()) # Output: dict_items([('name', 'John'),('age', 30), ('city', 'NewYork')])

#pop(key, default): Removes the key-value pair with the specified key and returns its value. If the key is not found, it returns the default value.
print(my_dict.pop('age')) # Output: 30
print(my_dict) # Output: {'name': 'John', 'city': 'New York'}
#popitem(): Removes and returns the last key-value pair inserted into the dictionary as a tuple.
print(my_dict.popitem()) # Output: ('city', 'New York')
print(my_dict) # Output: {'name': 'John', 'age': 30}
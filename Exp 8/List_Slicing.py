# my_list = [1, 2, 3, 4, 5]
# sub_list = my_list[1:3]
# print("Sliced list:", sub_list)
my_list = [1, 2, 3, "apple", "banana"]

# Slicing
sliced_list = my_list[1:4] # Elements from index 1 to 3
print(sliced_list) # Output: [ 2, 3, "apple"]
#Omitting Start or Stop:
print(my_list[:3]) # Elements from beginning to index 2
print(my_list[2:]) # Elements from index 2 to the end
#Negative Indices:
print(my_list[-3:]) # Last three elements of the list
#Stepping:You can specify a step value, which determines
#the increment between elements in the slice.
print(my_list[::2]) # Every second element of the list
#Reversing a List
#Slicing with a negative step value can reverse a list.
print(my_list[::-1]) # Reversed list
#Slicing can be used to make a shallow copy of a list.
new_list = my_list[:] # Copy the entire list

my_list[1] = "mango"
print(my_list) # Outputs: [1, 'mango', 3, 'apple', 'banana']
my_list[1:3] = [8, 9] # Replace elements at index 1 and 2
print(my_list)

my_list.append("cherry")
print(my_list) # Outputs: [1, 'mango', 3, 'apple', 'banana', 'cherry']

my_list.insert(1, "orange")
print(my_list) # Outputs: [1, 'orange', 'mango', 3, 'apple', 'banana', 'cherry']

my_list.remove("apple")# Removes the first occurrence of "apple"
print(my_list) # Outputs: [1, 'orange', 3, 'apple', 'banana', 'cherry']
my_list.pop(1) ## Removes element at index 1
print(my_list) # Outputs: [1, 3, 'apple', 'banana', 'cherry']

# my_list.sort()
# print(my_list) # Outputs: [1, 3, 'apple', 'banana', 'cherry']
# # It will give error as both are of different data type.
# my_list.sort(reverse=True)
# print(my_list) # Outputs: ['cherry', 'banana', 'apple', 3, 1]


another_list = [7, 8, 9]
my_list.extend(another_list)
# Alternatively you can use concatenation operator
x = [1,2,3]
y = x + [1,2,3]

x,y,z = [1,2,3] # Now x is 1, y is 2 \& z is 3
_,y = [1,2] # Underscore for a value which is thrown away

A =102 # A is integer data type
B= list(A) # B is List data type
A="Rohan" # A 's data type is string
B = list(A) # B's data type is list
#Advanced list
a = [1,2,3,4,5]
b = [5,4,3,6,1]
print(zip(a,b))
print(list(zip(a,b)))
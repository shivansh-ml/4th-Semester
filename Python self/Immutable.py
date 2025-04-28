x = 5 # x is an integer (immutable)
y = "hello" # y is a string (immutable)
z = (1, 2, 3) # z is a tuple (immutable)

# Immutable objects are objects whose state cannot be modified after they are created. When you modify the value of an
# immutable object, a new object is created in memory rather than modifying the existing one. 
# Immutable objects in Python include: integers, floats, complex numbers„booleans strings, tuples, frozensets.

x = 5
print(id(x))  # Memory address of integer 5

x+=1
print(id(x))  # Memory address of integer 6 (different from the previous one)

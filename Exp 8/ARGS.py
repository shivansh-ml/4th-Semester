# In Python, *args and **kwargs are used to pass a variable number of argu-
# ments to a function.

# • Using *args:
# *args is used to pass a variable number of positional arguments to a
# function. The * symbol unpacks the arguments into a tuple within the
# function.
def sum_values(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_values(1, 2, 3, 4, 5)) # Output: 15

# • **Using kwargs: **kwargs is used to pass a variable number of key-
# word arguments to a function. The ** symbol unpacks the keyword

# arguments into a dictionary within the function.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York")
# Output:

# name: Alice
# age: 30
# city: New York
# • **Using both *args and kwargs
def example_func(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)
    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
example_func(1, 2, 3, name="Alice", age=30)
# Output:
# Positional arguments:
# 1
# 2
# 3
# Keyword arguments:
# name: Alice
# age: 30
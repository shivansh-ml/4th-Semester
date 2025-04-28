# Syntax
# new_list = [expression for element in iterable if condition]
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares) # Output: [1, 4, 9, 16, 25]
# More examples
even_numbers=[x for x in range(5) if x % 2==0]
square_dict = {x : x *x for x in range(5)}
square_set = { x * x for x in [1,-1] }
# Multiple for
pairs = [(x,y) for x in range(10) for y in range(10)]
increasing_pairs = [(x,y) for x in range(10) for y in range(x+1,10)]
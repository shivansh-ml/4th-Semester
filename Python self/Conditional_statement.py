a = 10
if a > 0:
    print("a is positive")

a = -10
if a > 0:
    print("a is positive")
else:
    print("a is not positive")

a = 0
if a > 0:
    print("a is positive")
elif a < 0:
    print("a is negative")
else:
    print("a is zero")

a = 10
if a >= 0:
    if a == 0:
        print("a is zero")
    else:
        print("a is positive")
else:
    print("a is negative")

# Ternary Operator
# This is a shorthand version of the if-else statement. It allows you to test a 
# condition in a single line replacing the multi-line if-else making the code compact.
a = 10
print("a is positive") if a > 0 else print("a is not positive")
# The pass Statement: if statements cannot be empty, but if for some reason
# you have an if statement with no content, put in the pass statement to avoid
# getting an error.
a = 10
if a > 0:
    pass
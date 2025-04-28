# Arithmetic Operators
# These are used to perform mathematical operations.
a = 10
b = 20
print(a + b) # Addition: Outputs 30
print(a - b) # Subtraction: Outputs -10
print(a * b) # Multiplication: Outputs 200
print(a / b) # Division: Outputs 0.5
print(a % b) # Modulus: Outputs 10
print(a ** b) # Exponentiation: Outputs 100000000000000000000
print(a // b) # Floor division: Outputs 0

# Comparison Operators
# These are used to compare values

print(a == b) # Equal to: Outputs False
print(a != b) # Not equal to: Outputs True
print(a > b) # Greater than: Outputs False
print(a < b) # Less than: Outputs True
print(a >= b) # Greater than or equal to: Outputs False
print(a <= b) # Less than or equal to: Outputs True

# Logical Operators
# These are used to combine conditional statements.
a = True
b = False
print(a and b) # Logical AND: Outputs False
print(a or b) # Logical OR: Outputs True
print(not a) # Logical NOT: Outputs False

# Bitwise Operators
# These are used to compare binary numbers
a = 10 # binary: 1010
b = 4 # binary: 0100
print(a & b) # Bitwise AND: Outputs 0
print(a | b) # Bitwise OR: Outputs 14
print(~a) # Bitwise NOT: Outputs -11
print(a ^ b) # Bitwise XOR: Outputs 14
print(a >> 2) # Bitwise right shift: Outputs 2
print(a << 2) # Bitwise left shift: Outputs 40

# Assignment Operators
# These are used to assign values to variables.

a += 10 # Equivalent to a = a + 10: a becomes 20
a -= 10 # Equivalent to a = a - 10: a becomes 10
a *= 10 # Equivalent to a = a * 10: a becomes 100
a /= 10 # Equivalent to a = a / 10: a becomes 10.0
a %= 10 # Equivalent to a = a % 10: a becomes 0.0
a **= 10 # Equivalent to a = a ** 10: a becomes 0.0

# Membership Operators
# These are used to test whether a value or variable is in a sequence.
a = [1, 2, 3, 4, 5]
print(1 in a) # Outputs True
print(6 not in a)# Outputs True

# Identity Operators
# These are used to compare the memory locations of two objects.
a = 10
b = 10
print(a is b) # Outputs True
print(a is not b)# Outputs False
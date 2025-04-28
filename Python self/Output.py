print("Hello World")
#Separator and End Parameters:
#You can specify the separator between printed items and
#the string to be printed at the end using the sep and end
#parameters, respectively.
print("a", "b", "c", sep="-", end="***\n") # output a-b-c***
#Printing without a Newline:
#By default, print() ends with a newline character (\n).
#You can change this behavior by specifying the end parameter.
print("Hello", end="")
print("world!")

# Using formatted strings (f-strings) in Python 3.6 and later versions
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Using string concatenation
name = "Bob" 
age = 25
print("My name is "+name+" and I am "+str(age) + "years old.")

# Using the format() method
name = "Charlie"
age = 40
print("My name is {} and I am {} years old.".format(name, age))

# Using the %-formatting method (old-style formatting)
name = "Dave"
age = 35
print("My name is %s and I am %d years old." % (name, age))

# Using the sys.stdout.write() function from the sys module
import sys
sys.stdout.write("Hello, world!\n")

# Raw String Method "raw string" refers to a string that treats backslashes
# as literal characters, rather than as escape characters. You can create
# a raw string by prefixing the string literal with an r or R.
# Define a raw string
raw_string = r'C:\Users\Username\Desktop'
# Print the raw string
print(raw_string)

# Using file operations
with open("output.txt", "w") as f:
    print("Hello, file!", file=f)
#Alternative Method
with open("output.txt", "w") as file:
    file.write("This is written to a file.")
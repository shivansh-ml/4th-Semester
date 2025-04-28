# input() function:
user_input = input("Please enter something: ")
print("You entered: ", user_input)

# Command Line Arguments:
import sys
print("Script Name is: ", sys.argv[0])
print("First argument: ", sys.argv[1])
print("Second argument: ", sys.argv[2])

# File Input/Output:
with open('myfile.txt', 'r') as f:
    data = f.read()
    print(data)
text = "python programming"
#Capitalizes the first character of the string
print(text.capitalize()) # Output: Python programming
# Capitalizes the first letter of each word in the string.
print(text.title()) # Output: Python Programming
# Convert to lowercase and uppercase
print(text.lower()) # Output: 'python programming'
print(text.upper()) # Output: 'PYTHON PROGRAMMING'
# Replace substring
new_text = text.replace("Programming", "Code")
print(new_text) # Output: 'Python Code'
# Check if a substring exists
print('Python' in text) # Output: True
#Using find() or index()
my_string = "Python"
index_t = my_string.find('t') # 2
index_o = my_string.index('o') # 4
# Using split()
string = "hello world"
print(string.split()) # Output: ['hello', 'world']
# Using Join()
words = ['hello', 'world']
print(' '.join(words)) # Output: "hello world"
# Using startswith() and endswith()
string = "hello world"
print(string.startswith("hello")) # Output: True
print(string.endswith("world")) # Output: True
#Remove leading and trailing whitespace from the string.
string = " hello world "
print(string.strip()) # Output: "hello world"
print(string.lstrip()) # Output: "hello world "
print(string.rstrip()) # Output: " hello world"
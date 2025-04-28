strings = ["apple", "banana", "cherry", "date"]
word = input("Enter a word to search: ")
if word in strings:
    print(f"{word} is in the list")
else:
    print(f"{word} is not in the list")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(a == b):
    print("Both numbers are equal.")
elif(a != b):
    print("Both numbers are not equal.")
    if(a>b):
        print("First number is greater than second number.")
    else:
        print("Second number is greater than first number.")
try:
    numerator = 10
    denominator = 0
    result = numerator/denominator
    print(result)

except:
    print("Result cannot be zero")


try:
    even_number = [0,2,4,6]
    print(even_number[5])

except ZeroDivisionError:
    print("Result cannot be zero")
except IndexError:
    print("Index out of bound")

try:
    n = int(input("Enter a number: "))
    assert n%2 == 0
except:
    print("Not an Even number")
else:
    reciprocal = 1/n
    print(reciprocal)
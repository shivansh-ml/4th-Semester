def get_factors(num):
    factors = [i for i in range(1, num + 1) if num % i == 0]
    return factors

num = int(input("Enter a number: "))
print(get_factors(num))

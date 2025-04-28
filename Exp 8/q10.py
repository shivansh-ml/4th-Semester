numbers = list(range(1, 21))
count = 0
for num in numbers:
    if num % 2 == 0:
        print(num)
        count += 1
print(f"Count of even numbers: {count}")


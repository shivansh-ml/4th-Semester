numbers = [5, 3, 8, -1, -2.2, 0]
min_value = numbers[0]
for num in numbers[1:]:
    if num < min_value:
        min_value = num
print(f"Minimum value: {min_value}")

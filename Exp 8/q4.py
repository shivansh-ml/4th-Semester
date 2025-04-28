A = int(input("Enter A: "))
B = int(input("Enter B: "))

count = 0
while A % B == 0:
    A = A // B
    count += 1
if count > 0:
    print(f"Divisible {count} times")
else:
    print("Not divisible")

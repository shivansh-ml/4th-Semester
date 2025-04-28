count = 0
total = 0
while True:
    num = int(input("Enter a number (-1 to quit): "))
    if num == -1:
        break
    total += num
    count += 1

if count > 0:
    print(f"Average: {total / count}")
else:
    print("No numbers entered")

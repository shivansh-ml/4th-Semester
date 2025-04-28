# For Loop
# Iterating over a list
for i in [1, 2, 3, 4, 5]:
    print(i)

# While Loop
# Iterating until a condition is met
i = 1
while i <= 5:
    print(i)
    i += 1

# Nested loop
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)

for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
    print(i)

for i in [1, 2, 3, 4, 5]:
    if i == 3:
        continue
    print(i)

for i in [1, 2, 3, 4, 5]:
    pass
def check_divisibility(A, B):
    count = 0
    while A % B == 0:
        A //= B
        count += 1
    print(f"A is divisible by B {count} times.")
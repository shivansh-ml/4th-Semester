data = [1, "hello", 3.14, True, None, [1, 2], {'a': 1}, (3, 4), {1, 2}, b'byte']
for item in data:
    print(f"{item} -> {type(item)}")

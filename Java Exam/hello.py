def modify(lst):
    lst.append(100)
    lst = [200]
    return lst

a = [1, 2, 3]
b = modify(a)
print(a, b)
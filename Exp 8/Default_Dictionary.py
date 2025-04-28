from collections import defaultdict
d = defaultdict(int)
d['a']=1
d['b']=2
print(d['a'])
print(d['b'])
print(d['c'])
def default_value():
    return "default"
d1 = defaultdict(default_value)
d1['a']=1
d1['b']=2
print(d1['a'])
print(d1['b'])
print(d1['c'])
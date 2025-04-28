# Constructor overloading is not possible in Python. If we define multiple con-
# structors then the last constructor will be considered.

# class Test:
#     def __init__(self, a, b):
#         print("Two arg method")
#     def __init__(self, a):
#         print("One arg method")
#     def __init__(self):
#         print("No argument")
# t1 = Test()
'''Default Arguments'''
class Test:
    def __init__(self,a=None,b=None,c=None):
        print('Constructor with 0|1|2|3 number of arguments')
t1=Test()
t2=Test(1)
t3=Test(1,2)
t4=Test(2,3,4)
'''Variable Arguments'''
class T:
    def __init__(self,*args):
        print(args)
        if len(args) == 2:
            print("Two arg method")
        elif len(args) == 1:
            print("One arg method")
        elif len(args)>2:
            print("More than two arg method")
        else:
            print("No argument method")
t1=T(1,2,3,4,5)
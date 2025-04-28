# class Test:
#     def m1(self):
#         print("no-arg method")
#     def m1(self, a):
#         print("one-arg method")
#     def m1(self, a, b):
#         print("two-arg method")
# t =Test()
# # t.m1()  # prints "no-arg method"
# # t.m1(1)  # prints "one-arg method"
# t.m1(2,5)

# in Python Method overloading is not possible. If we are trying to declare
# multiple methods with same name and different number of arguments then
# Python will always consider only last method.
'''Default Arguments'''
class Test:
    def __init__(self,a=None,b=None,c=None):
        if(a!=None and b!=None and c!=None):
            print("Sum is: ",a+b+c)
        elif(a!=None and b!=None):
            print("Sum is:",a+b)
        else:
            print("Please send two or three arguments")
t= Test(1,2,3)
t = Test(1,2)  # prints "Sum is: 3"
t = Test(1)  # prints "Please send two or three arguments"
        
'''Variable Arguments'''
class T:
    def sum(self,*args):
        total = 0
        for i in args:
            total += i
        print("The sum",total)
t=T()
t.sum(10,20)
t.sum(10,30,20)
t.sum(10)
t.sum()
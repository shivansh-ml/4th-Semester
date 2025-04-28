class Test:
    x = 10 #Public Attribute
    _y = 20 #Protected Attribute
    __z = 30 #Private Attribute
    def m1(self):
        print(Test.x)
        print(Test._y)
        print(Test.__z)

t=Test()
t.m1()
print(Test.x)
print(Test._y)
print(Test.__z) #AttributeError: type #object 'Test' has no attribute '__z'
# By default every attribute is public. We can access from anywhere either
# within the class or from outside of the class.
# Eg: name = ’John’
# Protected attributes can be accessed within the class anywhere but from
# outside of the class only in child classes. We can specify an attribute as
# protected by prefexing with _ symbol.
# Syntax: _variablename = value
# Eg: _name=’John’
# But is is just convention and in reality does not exists protected attributes.
# Private attributes can be accessed only within the class.i.e from outside of
# the class we cannot access. We can declare a variable as private explicitly
# by prefexing with 2 underscore symbols.
# syntax: __variablename=value Eg: __name=’John’
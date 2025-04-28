class P:
    def m1():
        print("Parent Class")
class C1(P):
    def m2():
        print("Child 1 Class")
class C2(P):
    def m2():
        print("Child 2 Class")
c1=C1()
c2=C2()
C1.m2()
C1.m1()
C2.m2()
C2.m1()
class P:
    def m1(self):
        print("Parent 1 class")
class M:
    def m2(self):
        print("Parent 2 class")
class C(M,P):
    def m(self):
        print("Child Class")
c=C()
c.m1()
c.m2()
c.m()
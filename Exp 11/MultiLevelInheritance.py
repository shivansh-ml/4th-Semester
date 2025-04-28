class Gp:
    def m1(self):
        print("Grandparent class")
class P(Gp):
    def m2(self):
        print("Parent class")
class C(P):
    def m3(self):
        print("Child class")
c=C()
c.m3()
c.m2()
c.m1()
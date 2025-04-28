class P:
    a=10
    def __init__(self):
        self.b = 10
    def m1(self):
        print("Parent Insurance Method")
    @classmethod
    def m2(cls):
        print("Parent Class Method")
    @staticmethod
    def m3():
        print("Parent Static Method")
    
class C(P):
    a=888
    def __init__(self):
        self.b=999
        super().__init__()
        print(super().a)
        super().m1()
        super().m2()
        super().m3()
c=C()

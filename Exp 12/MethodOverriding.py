class P:
    def property(self):
        print('Gold+Land+Cash+Power')
    def marry(self):
        print('Appalamma')
class C(P):
    def marry(self):
        print('Timmy')
class D(P):
    def marry(self):
        super().marry()
        print('Timmy')

c=P()
cq=C()
c.property()
c.marry()
cq.property()
cq.marry()
d=D()
d.property()
d.marry()
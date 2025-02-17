import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
    def LenSquareCir(self):
        lent = 2*self.radius*math.pi
        sqr = math.pi*math.pow(self.radius,2)
        print(lent, sqr)
cir1 = Circle(5)
cir2 = Circle(6)
cir3 = Circle(10)
cir4 = Circle(3)
cir5 = Circle(2)
cir1.LenSquareCir()
cir2.LenSquareCir()
cir3.LenSquareCir()
cir4.LenSquareCir()
cir5.LenSquareCir()
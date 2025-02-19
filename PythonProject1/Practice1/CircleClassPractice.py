import math

class Circle():
    def __init__(self, radius):
        self.radius = radius
    def LenSquareCir(self):
        lent = 2*self.radius*math.pi
        sqr = math.pi*math.pow(self.radius,2)
        return lent, sqr

    @property
    def Color(self):
        return 'Red' if self.radius>5 else 'Blue'
cir1 = Circle(5)
cir2 = Circle(6)
cir3 = Circle(10)
cir4 = Circle(3)
cir5 = Circle(2)
print(cir1.LenSquareCir(),cir1.Color)
print(cir2.LenSquareCir(),cir2.Color)
print(cir3.LenSquareCir(),cir3.Color)
print(cir4.LenSquareCir(),cir4.Color)
print(cir5.LenSquareCir(),cir5.Color)
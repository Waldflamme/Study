class Car():
    def __init__(self, brand, model, ProdYear, mileage):
        self.brand = brand
        self.model = model
        self.ProdYear = ProdYear
        self.mileage = mileage
        self.TechServ = TechServ()

    def Info(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Year of production: {self.ProdYear}, Mileage: {self.mileage}')
        if self.mileage > 10000:
            print(self.TechServ.ts)

class TechServ():
    def __init__(self, lastts, ts):
        self.lastts = lastts
        self.ts = ts
        if self.lastts>10000:
            self.ts = 'Need Tech Service'
        else:
            self.ts = 'Doesnt need Tech Servie'

car1 = Car('Mazda','RX-7',1997,30000)
ts1 = TechServ(20000, 'ts')
car2 = ()
car3 = ()
car4 = ()
car5 = ()
print(car1.Info())
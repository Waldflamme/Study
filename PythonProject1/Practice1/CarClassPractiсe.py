class Car():
    def __init__(self, brand, model, ProdYear, mileage, LastTSMileage):
        self.brand = brand
        self.model = model
        self.ProdYear = ProdYear
        self.mileage = mileage
        self.LastTSMileage = LastTSMileage

    def Info(self):
        if self.mileage-self.LastTSMileage>=10000:
            return f'Brand: {self.brand} Model: {self.model} Year of production: {self.ProdYear} Mileage: {self.mileage} Tech Service: Needs TS'
        else:
            return f'Brand: {self.brand} Model: {self.model} Year of production: {self.ProdYear} Mileage: {self.mileage} Tech Service: Doesnt need TS'

    @property
    def GasType(self):
        if self.ProdYear > 2000:
            return 'Gas'
        elif self.ProdYear > 1990:
            return 'Diesel'
        else:
            return 'Vodka'
car1 = Car('Mazda','RX-7',1997,30000, 20000)
car2 = Car('BMW', 'M3', 2010, 30000, 25000)
car3 = Car('Volvo', 'C-90', 2015, 35000, 55000)
car4 = Car('Toyota', 'Supra', 1995, 90000, 87000)
car5 = Car('Lada', '2110', 1980, 530000, 10000)
print(car1.Info(),car1.GasType)
print(car2.Info(),car2.GasType)
print(car3.Info(),car3.GasType)
print(car4.Info(),car4.GasType)
print(car5.Info(),car5.GasType)
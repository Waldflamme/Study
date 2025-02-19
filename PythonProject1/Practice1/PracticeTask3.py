class Car():
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.FuelTank = FuelTank ()
class FuelTank():
    def __init__(self, volume = 40, gas_type = 95):
        self.volume = volume
        self.gas_type = gas_type

car1 = Car('BMW','x3',2023)
print(car1.brand,car1.model,car1.year,car1.FuelTank.volume,car1.FuelTank.gas_type)
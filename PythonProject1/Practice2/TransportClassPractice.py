class Transport():

    def __init__(self):
        pass

    def Info(self):
        pass

    def MaxWeight(self):
        pass

class Car(Transport):

    def __init__(self, brand, number, speed, max_weight):
        self.brand = brand
        self.number = number
        self.speed = speed
        self.max_weight = max_weight

    def Info(self):
        return f'Brand: {self.brand} Number: {self.number} Speed: {self.speed}'

    def MaxWeight(self):
        return f'Max weight: {self.max_weight}'

class Bike(Transport):

    def __init__(self,brand, number, speed, max_weight, sidecar):
        self.brand = brand
        self.number = number
        self.speed = speed
        self.max_weight = max_weight
        self.sidecar = sidecar

    def Info(self):
        return f'Brand: {self.brand} Number: {self.number} Speed: {self.speed}'

    def MaxWeight(self):
        return f'Max weight: {self.max_weight}' if self.sidecar==True else 'Max weight: 0'


class Truck(Transport):

    def __init__(self, brand, number, speed, max_weight, trailer):
        self.brand = brand
        self.number = number
        self.speed = speed
        self.max_weight = max_weight
        self.trailer = trailer

    def Info(self):
        return f'Brand: {self.brand} Number: {self.number} Speed: {self.speed}'

    def MaxWeight(self):
        return f'Max weight: {self.max_weight*2}' if self.trailer == True else f'Max weight: {self.max_weight}'

car = Car('BMW', 2130, '130 km/h', 100)
bike = Bike('BMW', 3450, '180 km/h', 50, False)
truck = Truck('Man', 3200, '300 km/h', 1000, True)
print(car.Info(),car.MaxWeight())
print(bike.Info(),bike.MaxWeight())
print(truck.Info(),truck.MaxWeight())
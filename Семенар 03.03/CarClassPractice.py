class Car(object):

    def __init__(self, brand, model, prod_year):
        self.brand = brand
        self.model = model
        self.prod_year = prod_year

    def Info(self):
        pass

    def Car_rep_check(self):
        if self.prod_year <= 1981:
            print('This car needs maintenance')
        else:
            print('This car does not need maintenance')

class LWCar(Car):

    def __init__(self, brand, model, prod_year, body_type):
        super().__init__(brand, model, prod_year)
        self.body_type = body_type

    def Info(self):
        return (f'Brand: {self.brand} Model: {self.model}'
                f' Year of production: {self.prod_year} Body type: {self.body_type}')

    def Car_age_check(self):
        if self.prod_year >= 2000:
            return f'This is a new car'
        else:
            return f'This is an old car'

    def car_search_model(self, mod):
        if self.model == mod:
            print(f'Info on car: {self.Info()}')
        else:
            pass

    def car_search_year(self, year):
        if self.prod_year == year:
            print(f'Info on car: {self.Info()}')
        else:
            pass

class BWCar(Car):

    def __init__(self, brand, model, prod_year, max_weight):
        super().__init__(brand, model, prod_year)
        self.max_weight = max_weight

    def Info(self):
        return (f'Brand: {self.brand} Model: {self.model} '
                f'Year of production: {self.prod_year} Maximum weight: {self.max_weight}')

    def Car_age_check(self):
        if self.prod_year >= 2000:
            return f'This is a new car'
        else:
            return f'This is an old car'

    def car_search_model(self, mod):
        if self.model == mod:
            print(f'Info on car: {self.Info()}')
        else:
            pass

    def car_search_year(self, year):
        if self.prod_year == year:
            print(f'Info on car: {self.Info()}')
        else:
            pass


class Bus(Car):

    def __init__(self, brand, model, prod_year, places_num):
        super().__init__(brand, model, prod_year)
        self.places_num = places_num

    def Info(self):
        return (f'Brand: {self.brand} Model: {self.model}'
                f' Prod_year: {self.prod_year} Number of seats:{self.places_num}')

    def Car_age_check(self):
        if self.prod_year >= 2000:
            return f'This is a new car'
        else:
            return f'This is an old car'

    def car_search_model(self, mod):
        if self.model == mod:
            print(f'Info on car: {self.Info()}')
        else:
            pass

    def car_search_year(self, year):
        if self.prod_year == year:
            print(f'Info on car: {self.Info()}')
        else:
            pass

car1 = LWCar('BMW', 'f1', 1981, 'hatchback')
car2 = BWCar('BMW', '2119', 1982, 5000)
car3 = Bus('Man', 'S21', 1981, 50)

car_list = [car1, car2, car3]

def base_output(lst):
    for i in lst:
        print(i.Info(), i.Car_age_check())

def car_list_search_model(lst):
    mod = input('Enter car model: ')
    for i in lst:
        i.car_search_model(mod)

def car_list_search_year(lst):
    year = int(input('Enter production year: '))
    for i in lst:
        i.car_search_year(year)

base_output(car_list)
car_list_search_model(car_list)
car_list_search_year(car_list)


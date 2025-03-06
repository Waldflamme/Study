class Goods(object):

    def __init__(self, name, manufacturer, price):
        self.name = name
        self.manufacturer = manufacturer
        self.price = price

    def info(self):
        pass

    def goods_price_check(self):
        if self.price <= 30:
            print('This product is cheap')
        else:
            print('This product is expensive')

class Electronics(Goods):

    def __init__(self, name, manufacturer, price, dev_type):
        super().__init__(name, manufacturer, price)
        self.dev_type = dev_type

    def info(self):
        return (f'Name: {self.name} Manufacturer: {self.manufacturer}'
                f' Price: {self.price} Device type: {self.dev_type}')

    def goods_search_name(self, name):
        if self.name == name:
            print(f'Info on product: {self.info()}')
        else:
            pass

    def goods_search_price(self, price):
        if self.price == price:
            print(f'Info on product: {self.info()}')
        else:
            pass

class Clothes(Goods):

    def __init__(self, name, manufacturer, price, size):
        super().__init__(name, manufacturer, price)
        self.size = size

    def info(self):
        return (f'Name: {self.name} Manufacturer: {self.manufacturer} '
                f'Price: {self.price} Size: {self.size}')

    def goods_search_name(self, name):
        if self.name == name:
            print(f'Info on product: {self.info()}')
        else:
            pass

    def goods_search_price(self, price):
        if self.price == price:
            print(f'Info on product: {self.info()}')
        else:
            pass


class Food(Goods):

    def __init__(self, name, manufacturer, price, exp_date):
        super().__init__(name, manufacturer, price)
        self.exp_date = exp_date

    def info(self):
        return (f'Name: {self.name} Manufacturer: {self.manufacturer}'
                f' Price: {self.price} Expire date:{self.exp_date}')


    def goods_search_name(self, name):
        if self.name == name:
            print(f'Info on product: {self.info()}')
        else:
            pass

    def goods_search_price(self, price):
        if self.price == price:
            print(f'Info on product: {self.info()}')
        else:
            pass

prod1 = Electronics('T-012', 'BOSH', 5000, 'Mixer')
prod2 = Clothes('00232', 'Uniclo', 2000, 'M')
prod3 = Food('Rice', 'China', 25, 2030)

goods_list = [prod1, prod2, prod3]

def base_output(lst):
    for i in lst:
        print(i.info(), i.goods_price_check())

def goods_list_search_name(lst):
    name = input('Enter product name: ')
    for i in lst:
        i.goods_search_name(name)

def goods_list_search_price(lst):
    price = int(input('Enter product price: '))
    for i in lst:
        i.goods_search_price(price)

base_output(goods_list)
goods_list_search_name(goods_list)
goods_list_search_price(goods_list)
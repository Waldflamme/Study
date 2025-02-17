class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def Leftovers(self):
        return 'In Stock' if self.quantity>0 else 'Out of stock'

prod1 = Product('rice',1.55,0)
prod2 = Product('Pork', 2.55, 100)
prod3 = Product('Beef', 4.50,200)
prod4 = Product('Rosmarine', 1.35,0)
prod5 = Product('Pease',1,35)
print(f'Product 1: {prod1.Leftovers()}')
print(f'Product 2: {prod2.Leftovers()}')
print(f'Product 3: {prod3.Leftovers()}')
print(f'Product 4: {prod4.Leftovers()}')
print(f'Product 5: {prod5.Leftovers()}')
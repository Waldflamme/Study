class Shop(object):

    def __init__(self, name, prod_list = []):
        self.name = name
        self.prod_list = prod_list

    def ProdAdd(self):
        name = input('Введите имя: ')
        price = input('Введите цену: ')
        quant = input('Введите количество: ')
        prod = Prod(name, price, quant)
        self.prod_list.append(prod)

    def Info(self):
        for i in range(0, len(self.prod_list)):
            print(self.prod_list[i].Info())

    def ProdSum(self):
        x = 0
        for i in range(0, len(self.prod_list)):
            x+=self.prod_list[i].ProdSum()
        print(f'Сумма товаров: {x}')

    def ProdDel(self,ind):
        del self.prod_list[ind]

    def __len__(self):
        return self.prod_list.__len__()

class Prod(Shop):

    def __init__(self, name, price, quant):
        self.name = name
        self.price = price
        self.quant = quant

    def Info(self):
        return f'{self.name} {self.price} {self.quant}'

    def ProdSum(self):
        return int(self.price)*int(self.quant)

shop1 = Shop('Хозяйка')
shop1.ProdAdd()
shop1.ProdAdd()
shop1.Info()
shop1.ProdSum()
#shop1.ProdDel(1)
#shop1.Info()
print(shop1.__len__())

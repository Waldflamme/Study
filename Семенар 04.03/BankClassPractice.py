class Bank(object):

    def __init__(self, name, acc_list = []):
        self.name = name
        self.acc_list = acc_list

    def AccAdd(self):
        num = input('Введите номер: ')
        balance = input('Введите баланс: ')
        acc = Acc(num, balance)
        self.acc_list.append(acc)

    def Info(self):
        for i in range(0, len(self.acc_list)):
            print(self.acc_list[i].Info())

    def BalSum(self):
        x = 0
        for i in range(0, len(self.acc_list)):
            x+=self.acc_list[i].BalVal()
        print(f'Сумма балансов: {x}')

    def AccDel(self,ind):
        del self.acc_list[ind]

    def __len__(self):
        return self.acc_list.__len__()

class Acc(Bank):

    def __init__(self, num, balance):
        self.num = num
        self.balance = balance

    def Info(self):
        return f'{self.num} {self.balance}'

    def BalVal(self):
        return int(self.balance)

Bank1 = Bank(input('Введите название банка: '))
Bank1.AccAdd()
Bank1.AccAdd()
Bank1.AccAdd()
Bank1.Info()
Bank1.BalSum()
Bank1.AccDel(1)
Bank1.Info()
print(f'Количество счетов: {Bank1.__len__()}')

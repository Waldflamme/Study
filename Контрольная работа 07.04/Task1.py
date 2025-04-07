
class Client(object):
    def __init__(self, date):
        self.date = date

    def info(self):
        pass

    def match_date(self, date):
        search_date = date
        return self.date == search_date


class Depositor(Client):
    def __init__(self, surname, opening_date, deposit_volume, interest_rate):
        super().__init__(opening_date)
        self.surname = surname
        self.deposit_volume = deposit_volume
        self.interest_rate = interest_rate

    def info(self):
        print(f"Surname: {self.surname}, Opening Date: {self.date}, "
              f"Deposit Volume: {self.deposit_volume}, Interest Rate: {self.interest_rate}%")


class Creditor(Client):
    def __init__(self, surname, credit_date, credit_volume, interest_rate, remaining_debt):
        super().__init__(credit_date)
        self.surname = surname
        self.credit_volume = credit_volume
        self.interest_rate = interest_rate
        self.remaining_debt = remaining_debt

    def info(self):
        print(f"Surname: {self.surname}, Credit Date: {self.date}, "
              f"Credit Volume: {self.credit_volume}, Interest Rate: {self.interest_rate}%, Remaining Debt: {self.remaining_debt}")


class Organization(Client):
    def __init__(self, name, account_opening_date, account_number, account_balance):
        super().__init__(account_opening_date)
        self.name = name
        self.account_number = account_number
        self.account_balance = account_balance

    def info(self):
        print(f"Name: {self.name}, Account Opening Date: {self.date}, "
              f"Account Number: {self.account_number}, Account Balance: {self.account_balance}")


clients = [
    Depositor("Ivanov", "15.01.2023", 50000, 5.5),
    Creditor("Petrov", "15.01.2023", 100000, 12.0, 60000),
    Organization("CreamSoda", "01.12.2022", "40817810099910004321", 1500000),
    Depositor("Sidorov", "10.03.2022", 30000, 4.7)
]

for i in clients:
    i.info()

print()

search_date = "15.01.2023"
for i in clients:
    if i.match_date(search_date):
        i.info()
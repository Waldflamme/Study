class PhoneBookEntry(object):
    def info(self):
        pass

    def matches_surname(self, surname):
        return False


class Person(PhoneBookEntry):
    def __init__(self, surname, address, phone):
        self.surname = surname
        self.address = address
        self.phone = phone

    def info(self):
        print(f"Surname: {self.surname}, Address: {self.address}, Phone: {self.phone}")

    def matches_surname(self, surname):
        return self.surname == surname


class Organization(PhoneBookEntry):
    def __init__(self, name, address, phone, fax, contact_person):
        self.name = name
        self.address = address
        self.phone = phone
        self.fax = fax
        self.contact_person = contact_person

    def info(self):
        print(f"Name: {self.name}, Address: {self.address}, Phone: {self.phone}, "
              f"Fax: {self.fax}, Contact Person: {self.contact_person}")


class Friend(Person):
    def __init__(self, surname, address, phone, birth_date):
        super().__init__(surname, address, phone)
        self.birth_date = birth_date

    def info(self):
        print(f"Surname: {self.surname}, Address: {self.address}, Phone: {self.phone}, "
              f"Birth Date: {self.birth_date}")


phone_book = [
    Person("Ivanov", "Moscow, Arbat 12", "+7(495)123-45-67"),
    Organization("CreamSoda", "St. Petersburg, Nevsky 45", "+7(812)234-56-78", "+7(812)234-56-79", "Petrov"),
    Friend("Sidorov", "Kazan, Bauman 5", "+7(843)345-67-89", "15.06.1996"),
    Person("Smirnov", "Moscow, Arbat 33", "+7(495)987-65-43")
]

for i in phone_book:
    i.info()

print()

search_surname = "Sidorov"
for i in phone_book:
    if i.matches_surname(search_surname):
        i.info()
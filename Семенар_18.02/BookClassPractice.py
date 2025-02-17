class Book():
    def __init__(self, name, author, publisher, PublishYear):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.PublishYear = PublishYear
    def OutPut(self):
        print(f'Name:{self.name}, Author:{self.author}, Publisher:{self.publisher}, Year of publishmen:{self.PublishYear}')
book1 = Book('HarryPotter1','Joan Roalling','Owl',2001)
book2 = Book('HarryPotter2','Joan Roalling','Owl',2002)
book3 = Book('HarryPotter3','Joan Roalling','Owl',2003)
book4 = Book('HarryPotter4','Joan Roalling','Owl',2004)
book5 = Book('HarryPotter5','Joan Roalling','Owl',2005)
print(book1.OutPut())
print(book2.OutPut())
print(book3.OutPut())
print(book4.OutPut())
print(book5.OutPut())
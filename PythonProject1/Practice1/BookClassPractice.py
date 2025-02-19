class Book():

    def __init__(self, name, author, publisher, PublishYear):
        self.name = name
        self.author = author
        self.publisher = publisher
        self.PublishYear = PublishYear
        self.genre = 'Fantasy'
    def OutPut(self):
        return f'Name:{self.name}, Author:{self.author}, Publisher:{self.publisher}, Year of publishmen:{self.PublishYear}'
    def New(self):
        return 'This is a new book' if 2008-self.PublishYear<5 else 'This is an old book'

    @property
    def Genre(self):
        return self.genre

book1 = Book('HarryPotter1','Joan Roalling','Owl',2001)
book2 = Book('HarryPotter2','Joan Roalling','Owl',2002)
book3 = Book('HarryPotter3','Joan Roalling','Owl',2003)
book4 = Book('HarryPotter4','Joan Roalling','Owl',2004)
book5 = Book('HarryPotter5','Joan Roalling','Owl',2005)
print(f'{book1.OutPut()} Is it new?: {book1.New()} Genre: {book1.Genre}')
print(f'{book2.OutPut()} Is it new?: {book2.New()} Genre: {book2.Genre}')
print(f'{book3.OutPut()} Is it new?: {book3.New()} Genre: {book3.Genre}')
print(f'{book4.OutPut()} Is it new?: {book4.New()} Genre: {book4.Genre}')
print(f'{book5.OutPut()} Is it new?: {book5.New()} Genre: {book5.Genre}')
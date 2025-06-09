class Book:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = int(year)

    def __str__(self):
        return f"{self.author} — \"{self.title}\" ({self.year})"

def read_books_from_file(filename):
    books = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split(';')
            if len(parts) != 3:
                continue
            author, title, year = parts
            books.append(Book(author, title, year))
    return books

def bubble_sort(books, key):
    n = len(books)
    for i in range(n):
        for j in range(0, n - i - 1):
            if getattr(books[j], key) > getattr(books[j + 1], key):
                books[j], books[j + 1] = books[j + 1], books[j]
    return books

def insertion_sort(books, key):
    for i in range(1, len(books)):
        current = books[i]
        j = i - 1
        while j >= 0 and getattr(books[j], key) > getattr(current, key):
            books[j + 1] = books[j]
            j -= 1
        books[j + 1] = current
    return books

def print_books(books):
    for book in books:
        print(book)

if __name__ == "__main__":
    books = read_books_from_file("books.txt")

    sort_key = input("Сортировать по (author/title/year): ").strip()
    method = input("Метод сортировки (bubble/insertion): ").strip()

    if sort_key not in ['author', 'title', 'year']:
        print("Ошибка: недопустимый ключ сортировки.")
    elif method == 'bubble':
        sorted_books = bubble_sort(books.copy(), sort_key)
        print_books(sorted_books)
    elif method == 'insertion':
        sorted_books = insertion_sort(books.copy(), sort_key)
        print_books(sorted_books)
    else:
        print("Ошибка: недопустимый метод сортировки.")
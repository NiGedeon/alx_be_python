class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def __str__(self):
        return (f"{self.title} by {self.author}")

class EBook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return (f"{self.title} by {self.author} {self.file_size}")


class PrintBook(Book):
    def __init__(self, title, author,page_count):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
         return (f"{self.title} by {self.author} {self.page_count}")


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if isinstance(book,Book):
            self.books.append(book)
        else:
            raise TypeError("The 'book' must be an instance of 'Book', or 'EBook', or 'PrintBook!'")

    def list_books(self):
        for book in self.books:
            if isinstance(book, Book):
                print(f"Book: {book.title} by {book.author}")
            elif isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")


from collections import defaultdict
from book import Book


class Library:
    __COUNTER_ID = 0

    def __init__(self, name):
        self.__name = name
        self.__id = None
        self.__set_id()
        self.__size = 100
        self.__books = defaultdict(list)

    def __set_id(self) -> None:
        self.__id = self.__COUNTER_ID
        self.__COUNTER_ID += 1

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> int:
        return self.__id

    def add_book(self, book: Book) -> None:
        if book in self.__books[book.get_key()]:
            print("This book already is added in this library")
        else:
            self.__books[book.get_key()].append(book)

    def pop_book(self, book: Book) -> bool:
        if book.get_key() in self.__books:
            self.__books[book.get_key()].remove(book)
            return True
        return False

    def show_library(self):
        print("Books of", self.get_name(), "`", end='  ')
        if len(self.__books) == 0:
            print("Library is empty")
        for books in self.__books.values():
            for book in books:
                print((book.get_title(), book.get_author()), end='  ')
        print()

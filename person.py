from library import Library
from book import Book


class Person:
    def __init__(self, name: str, surname: str):
        self.__name = name
        self.__surname = surname
        self.__books = {}

    def get_name(self) -> str:
        return self.__name

    def get_surname(self) -> str:
        return self.__surname

    def take_book(self, book: Book, library: Library):
        if (book, library.get_id()) in self.__books.items():
            return "Դուք այդ գրադարանից արդեն վերձրել եք այդ գրքից:Նույն գրադարանից հնարավոր չէ վերջնել երկու նույն " \
                   "գրքից "
        if library.pop_book(book):
            self.__add_book(book, library)
        else:
            print("This library dont have that book")

    def __add_book(self, book: Book, library: Library) -> None:
        self.__books[book] = library

    def give_back_book(self, book: Book) -> None:
        if book in self.__books:
            self.__books[book].add_book(book)
            self.__pop_book(book)
        else:
            print("Դուք չունեք նման գիրք")

    def __pop_book(self, book: Book) -> None:
        del self.__books[book]

    def show_books(self):
        print("Books of", self.get_name(), "`", end='  ')
        if len(self.__books) == 0:
            print("This person dont have books")
        for book in self.__books:
            print((book.get_title(), book.get_author()))

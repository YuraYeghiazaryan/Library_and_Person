from library import Library
from book import Book
from person import Person

# create some books
book1 = Book("Booch", "OOAD")
book2 = Book("Slatkin", "Effektive Python")
book3 = Book("Shildt", "Java")
book4 = Book("Yura", "Pandas Handbook")
book5 = Book("David Bizly", "Python")

# create two libraries
lib1 = Library("Picsart")
lib2 = Library("Politexnik")
print("1. before adding books`", end='  ')
lib1.show_library()  # 1

# create two persons
person1 = Person('Yura', 'Yeghiazaryan')
person2 = Person('Areg', 'Sedrakyan')

# add book1,book2 in library1
lib1.add_book(book1)
lib1.add_book(book2)

# add book3,book4 in library2
lib2.add_book(book3)
lib2.add_book(book4)

# book5 don't add in any library

# show libraries
print("2. ", end='')
lib1.show_library()  # 2
print("3. ", end='')
lib2.show_library()  # 3

# show person's book
print('4. ', end='')
person1.show_books() # 4

# add than book, which is already added
print('5. ', end='')
lib1.add_book(book1) # 5

# create another object book, but with same author and title
book6 = Book("Booch", "OOAD")
# and add that book to lib1 where one already exists
lib1.add_book(book6)
# this book will be added because it is a different object and has a different id
print('5\'. ', end='')
lib1.show_library() # 5'


# take books from libraries by person
person1.take_book(book1, lib1)
person2.take_book(book3, lib2)

# show books of persons
print('6. ', end='')
person1.show_books() # 6
print('7. ', end='')
person2.show_books() # 7

# take book, which does not exist in that library
print('8. ', end='')
person1.take_book(book4, lib1) # 8

# library's books, after taking by persons
print('9. ', end='')
lib1.show_library() # 9
print('10. ', end='')
lib2.show_library() # 10

# give back book in library,it is automatically returned to the library from which it was borrowed
print('11. ', end='')
person1.give_back_book(book1)  # 11
person1.show_books()           # 11
lib1.show_library()            # 11

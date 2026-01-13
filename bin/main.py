from coers_library.book import Book
from coers_library.library import Library
from coers_library.user import User

if __name__ == '__main__':
    kak = Book('Алые паруса', 'Александр Грин', 1923)
    eto = Book("Божественная комедия", "Данте Алигьери", 1816)

    lib1 = Library('Flex')
    lib1.app_book(kak)
    lib1.app_book(eto)
    user1 = User('Фелекс')

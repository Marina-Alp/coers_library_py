from book import Book
from library import Library
from user import User

if __name__ == '__main__':
    kak = Book('Алые паруса', 'Александр Грин', 1923)
    eto = Book("Божественная комедия", "Данте Алигьери", 1816)
    iuo = Book('Дом Ужасов','Рульям Уйил',2012)

    lib1 = Library('Flex')
    lib1.app_book(kak)
    lib1.app_book(eto)
    lib1.del_book(kak)
    lib1.app_book(iuo)
    print(lib1)
    lib1.search('Дом Ужасов')
    lib1.search("Данте Алигьери")

    len_librere = len(lib1.list_books_in_library)
    print(f'Общая количество книг в библиотеке: {len_librere}')

    user1 = User('Фелекс')
    user1.app_reading_book(lib1, kak)
    user1.app_reading_book(lib1, eto)



from book import Book
from library import Library

class User:
    """
    Класс для создания списка читаемого пользователем книг в библиотеке
    """
    def __init__(self, name_user):
        """
        Базовый конструктор класса
        :param name_user: Имя пользователя
        list_books: Автоматически создающийся список книг пользователя
        """
        self.__name_user = name_user
        self._reading_list_books = []

    @property
    def user_reading(self):
        """
        Метод обращения к пользователю
        :return: Имя пользователя и список его книг
        """
        return self.__name_user + ': ' +str( self._reading_list_books)

    def __str__(self):
        """
        Выводит имя посетителя библиотеки и список его книг
        :return: f'Библиотека: "{имя посетителя библиотеки и список его книг}"'
        """
        return f'Карточка посетителя: "{self.user_reading}"'

    def app_reading_book(self, librari, its_book):
        """
        Метод проверяет есть ли заданная книга в библиотеки и если правда то добовляет в конец списка заданную книгу
        :param librari: библиотека из которой берут книгу (class Library)
        :param its_book: Книга которую берут (class Book)
        :return: Список книг
        """
        if its_book.full_name_book.strip().lower() in librari.list_books_in_library:
            self._reading_list_books.append(its_book.full_name_book.strip().lower())
            librari.del_book(its_book)
            print(f'{its_book} добавлина в ваш список')
        else: print(f'{its_book} нет в библиотеки')

    def return_book(self, libreri, returning_book):
        """
        Метод проверяет есть ли заданная книга у пользователя и если правда то удаляет заданную книгу из списка пользователя
        :param libreri: библиотека в которую возвращают книгу (class Library)
        :param returning_book: Книга которую возвращают (class Book)
        :return: Список книг
        """
        if returning_book.full_name_book.strip().lower() in self._reading_list_books:
            self._reading_list_books.remove(returning_book.full_name_book.strip().lower())
            libreri.app_book(returning_book)
            print(f'{returning_book} вычеркнута из вашего списка чтения')
        else: print("У вас нет этой книги")

if __name__ == '__main__':
    kak = Book('Алые паруса', 'Александр Грин', 1923)
    eto = Book("Божественная комедия", "Данте Алигьери", 1816)

    lib1 = Library('Flex')
    lib1.app_book(kak)
    lib1.app_book(eto)

    user1 = User('Фелекс')
    print(user1)
    print(lib1)
    user1.app_reading_book(lib1, kak)

    user1.return_book(lib1, eto)
    print(user1)
    print(lib1)



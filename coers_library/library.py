from book import Book

class Library:
    """
    Класс для создания библиотек в которых хранятся книги
    """
    def __init__(self, name):
        """
        Базовый конструктор класса
        :param name: Название библиотеки
        list_books: Автоматически создающийся список для сохранения книг
        """
        self.__name = name
        self._list_books = []

    @property
    def library(self):
        """
        Метод обращения к библиотеке
        :return: Наименование библиотеки и список её книг
        """
        return self.__name + ': ' +  str(self._list_books)

    @property
    def list_books_in_library(self):
        """
        Метод обращения к списку книг в библиотеке
        :return: список книг библиотеки
        """
        return self._list_books

    @library.deleter
    def library(self):
        """
        Метод удаляет библиотеку. И название библиотеки и список её книг
        :return: None
        """
        print(f'Библиотека {self.library} удалина')
        del self.__name
        del self._list_books

    def app_book(self, name_book):
        """
         Метод добовляет в конец списка заданную книгу
        :param name_book: 'Название книги, имя автора книги, год выпуска книги'
        :return: Список книг с новой добавленной книгой
        """
        self.list_books_in_library.append(name_book.full_name_book.strip().lower())
        print(f'{name_book} была добавлена в библиотеку')

    def del_book(self, name_del_book):
        """
        Метод дудаляет из библиотеки заданную книгу
        :param name_del_book: 'Название книги, имя автора книги, год выпуска книги'
        :return: Список книг без заданной книги
        """
        self.list_books_in_library.remove(name_del_book.full_name_book.strip().lower())
        print(f'{name_del_book} была удалина из библиотеки')

    def search(self, marker):
        """
        Метод ищит в библиотеки книги содержащие указанное название или автора книги
        :param marker: Название книги или автор книги
        :return: Список книг в которых есть указанное нзвание книги/автор книги
        """
        temp1 = []
        for book in self.list_books_in_library:
            if marker.strip().lower() in book:
                temp1.append(book)
        if len(temp1) == 0:
            print(f'Извините, книги  {marker} нет в библиотеке')
        else:
            print(f'Вот список книг  {marker}: {temp1}')
        return temp1

    def sorting(self, marker = None):
        """
        Метод сортирует книги в выбранном режиме. Всего режимомов три [0,1,2]
        0:'по названию', 1:'по автору', 2:'по дате
        :param marker: цифра выбраного режима.Изначально стаит на 0
        :return: Список книг отсортированных в указанном режиме
        """
        sorter_list_book = []
        sorting_modes = {0:'по названию', 1:'по автору', 2:'по дате'}
        if marker is None:
            marker = 0
        if marker not in sorting_modes:
            print('Такого метода сортировки нет попробуйте ещё раз')
            return None

        if len(self.list_books_in_library) == 0:
            print(f'Извините, книг нет в библиотеке')
        else:
            sorter_list_book = sorted(self.list_books_in_library, key= lambda mods: mods.strip().lower().split(',')[marker])
            print(f'Вот список книг отсортированный {sorting_modes[marker]}: {sorter_list_book}')

        return sorter_list_book

    def __str__(self): #__str__?
        """
        Выводит название библиотеки и список содержащихся в ней книг
        :return: f'Библиотека: "{название библиотеки и список её книг}"'
        """
        return f'Библиотека: "{self.library}"'


if __name__ == '__main__':
    kak = Book('jhg', 'djh?', 2012)
    eto = Book("ajhg", "ajh?", 2510)

    lib1 = Library('Flis')
    print(lib1)
    lib1.app_book(kak)
    print(lib1)
    lib1.app_book(eto)
    print(lib1)
    lib1.sorting(2)






#sorted(student_objects, key=lambda student: student.age)
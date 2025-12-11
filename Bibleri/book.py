class Book:
    '''
    Класс позволяет создовать книги
        создовая книги нужно ввести: название книги, имя автора и год выпуска
        пример: book1 = Book('The Call of Cthulhu','Lovecraft',1928)
    Класс позволяет изменять книги
        для этого нужно прировнять переменную к новому значению введя все новые переменные через запятую
        пример: book1 = 'Dagon, Lovecraft, 1919'
    Класс позволяет удалять книги
        для этого введите del и книгу которую желаите удалить
        пример del book1.full_name_book
    Класс позволяет смотреть выводить книги
        print(book1)
    Класс позволяет сравнивать книги
        book1.compare(book2)
    '''
    def __init__(self, name, author, year):
        self._name = name
        self._author = author
        self._year = year

    @property
    def full_name_book(self):
        return self._name + " " + self._author + " " + self._year

    @full_name_book.setter
    def full_name_book(self, new):
        self._name, self._author, self._year = new.split(",")

    @full_name_book.deleter
    def full_name_book(self):
        print(f"Книга '{self}' удалина")
        del self.full_name_book

    def print(self): #__str__?
        print(f'Это книга: {self.full_name_book}')

    def compare(self, compare_book):
        if self.full_name_book == compare_book:
            return True
        else: return False

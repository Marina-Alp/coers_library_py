import book
class Library:
    def __init__(self, list_books=None):
        if list_books is None:
            list_books = []
        self.list_books = list_books


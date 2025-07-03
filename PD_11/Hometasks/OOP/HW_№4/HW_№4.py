from __future__ import annotations

# Задание № 1

class Library:

    def __init__(self, name: str, address: str, books: list[Book] = []):

        if not isinstance(name, str): raise TypeError("Ошибка: Некорректные входные данные")
        if len(name) == 0: raise ValueError("Библиотека не может не иметь названия!")
        if not isinstance(address, str): raise TypeError("Ошибка: Некорректные входные данные")
        if isinstance(books, list):
            if len(books) != 0:
                for book in books:
                    if not isinstance(book, Book): raise TypeError("В списке книг библиотеки должны быть только книги!")
        else: raise TypeError("Ошибка: Некорректные входные данные")

        self._name = name
        self._address = address
        self._books = books

    def _addBook(self, book: Book):

        if not isinstance(book, Book): raise TypeError("В библиотеку можно добавить только книгу!")

        self._books.append(book)

    def _removeBook(self, book: Book):

        if not isinstance(book, Book): raise TypeError("Из библиотеки можно брать только книги!")
        if book in self._books: self._books.remove(book)
        else: raise ValueError("Данной книге в списке нет!")

    def _listBooks(self):
        for book in self._books:
            book._getInfo()

    def _findBookByTitle(self, required_title: str):

        if not isinstance(required_title, str): raise TypeError("Вы ввели некорректное наименование!")
        if len(required_title) == 0: raise ValueError("Книг без названия не существвует!")

        result = "Данная книга отсутствует!"
        for book in self._books:
            if required_title == book._title:
                result = book
                break
            return result


class Book:

    def __init__(self, title: str, author: str, year: int):

        if not isinstance(title, str): raise TypeError("Ошибка: Некорректный тип входных данных")
        if len(title) == 0: raise ValueError("Книга должна иметь название!")
        if not isinstance(author, str): raise TypeError("Ошибка: Некорректный тип входных данных")
        if len(author) == 0: raise ValueError("Книга должна иметь автора!")
        if not isinstance(year, int): raise TypeError("Ошибка: Некорректный тип входных данных")
        if year < 0 or year > 2025: raise ValueError("Книга не могла быть издана в данном году!")

        self._title = title
        self._author = author
        self._year = year

    def _getInfo(self):
        print(f"{self._title} - {self._author}, {self._year} г.")

    def _bookmarkPage(self, page: int):

        if not isinstance(page, int): raise TypeError("Некорректные входные данные")

        return f"Закладка размещена на {page}-й странице"

# Задание № 2





# Задание № 3





# Задание № 4
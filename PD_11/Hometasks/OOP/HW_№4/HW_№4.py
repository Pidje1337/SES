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

        self.__name = name
        self.__address = address
        self.__books = books

class Book:

    def __init__(self, title: str, author: str, year: int):

        if not isinstance(title, str): raise TypeError("Ошибка: Некорректный тип входных данных")
        if len(title) == 0: raise ValueError("Книга должна иметь название!")
        if not isinstance(author, str): raise TypeError("Ошибка: Некорректный тип входных данных")
        if len(author) == 0: raise ValueError("Книга должна иметь автора!")
        if not isinstance(year, int): raise TypeError("Ошибка: Некорректный тип входных данных")
        if year < 0 or year > 2025: raise ValueError("Книга не могла быть издана в данном году!")

        self.__title = title
        self.__author = author
        self.__year = year


# Задание № 2





# Задание № 3





# Задание № 4
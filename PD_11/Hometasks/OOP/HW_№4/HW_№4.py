from __future__ import annotations

# Примечание:
# Проверку данных и соответствие значений заданным интервалам не написал ради сохранения единой стилистики
# Сообщения в ValueError и TypeError не привёл к дожному виду для экономии времени

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
            self._books = books
        else: raise TypeError("Ошибка: Некорректные входные данные")

        self._name = name
        self._address = address

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

    def _updateTitle(self, new_title):

        if not isinstance(new_title, str): raise TypeError("Некорректное наименование!")
        if len(new_title) == 0: raise ValueError("Невозможно задать пустое название для книги!")

        self._title = new_title



# Задание № 2

class University:

    def __init__(self, name: str, faculties: list[Faculty]):

        if not isinstance(name, str): raise TypeError("Некорректные входные данные!")
        if len(name) == 0: raise ValueError("ВУЗ не может не иметь названия!")

        if isinstance(faculties, list):
            for faculty in faculties:
                if not isinstance(faculty, Faculty): raise TypeError("В данном списке могут находиться только факультеты!")
            self._faculties = faculties
        else: raise TypeError("Некорректные входные данные")

        self._name = name

    def _add_faculty(self, faculty: Faculty):

        if not isinstance(faculty, Faculty): raise TypeError("Некорректные входные данные")

        self._faculties.append(faculty)


class Faculty:

    def __init__(self, name: str, students: list[Student] = []):

        if not isinstance(name, str): raise TypeError("Некорректные входные данные")
        if len(name) == 0: raise ValueError("Факультет должен иметь название!")
        if isinstance(students, list):
            if len(students) != 0:
                for student in students:
                    if not isinstance(student, Student): raise TypeError("Некорректные входные данные!")
            self._students = students
        else: raise TypeError("Некорректные входные данные")

        self._name = name

    def enroll(self, student: Student):

        if not isinstance(student, Student): raise TypeError("Некорректные входные данные")
        if student in self._students: raise ValueError("Студент уже есть в списке!")
        self._students.append(student)

    def graduate(self, student: Student):

        if not isinstance(student, Student): raise TypeError("Некорректные входные данные")
        if student not in self._students: raise ValueError("Данного студента нет в списке!")
        self._students.remove(student)
        print(f"Студент {student._name} выпустился!")

    def list_students(self):
        for student in self._students:
            print(student)

    def fint_student(self, required_id):

        for student in self._students:
            if required_id == student._id: return student
        print("Данный студент не найден!")
        return None

class Student:

    def __init__(self, name: str, id: int, grades: list = []):

        if not isinstance(name, str): raise TypeError("Некорректные входные данные")
        if len(name) == 0: raise ValueError("Студент должен иметь ФИО!")
        if not isinstance(id, int): raise TypeError("Некорректные входные данные")
        if id < 0: raise ValueError("Номер зачётки не может быть отрицательным!")
        if isinstance(grades, list):
            if len(grades) != 0:
                for grade in grades:
                    if not isinstance(grade, int): raise TypeError("Отметка должна быть целым числом!")
                    if grade < 0 or grade > 100: raise ValueError("Отметка может принимать значения в пределах от 0 до 100!")
            self._grades = grades
        else:
            raise TypeError("Некорректные входные данные")

        self._name = name
        self._id = id

    def __str__(self):
        return f"Студент: {self._name}, ID: {self._id}"

    def get_profile(self):
        print(self)

    def assign_grade(self, grade: int):

        if not isinstance(grade, int): raise TypeError("Некорректные входные данные")
        if grade not in range(0, 101): raise ValueError("Оценка должна быть целым числом в пределах от 0 до 100!")

        self._grades.append(grade)



# Задание № 3





# Задание № 4
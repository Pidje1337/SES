from math import sqrt

# Задание № 1

class Vector2D:

    def __init__(self, x: int or float, y: int or float):

        if not isinstance(x, (int or float)): raise TypeError("Ошибка: x должно быть целым или вещественным числом")
        self.x = x
        if not isinstance(y, (int or float)): raise TypeError("Ошибка: y должно быть целым или вещественным числом")
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector2D): raise TypeError("Данный метод позволяет складывать только вектора!")
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector2D): raise TypeError("Данный метод позволяет вычитать только вектора!")
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int or float):
        if not isinstance(scalar, (int or float)): raise TypeError("Ошибка: Scalar должно быть целым или вещественным числом")
        return Vector2D(self.x * scalar, self.y * scalar)

    def __len__(self):
        return sqrt(sum(self.x ** 2, self.y ** 2))

    def __repr__(self):
        return f"Vector2D(x = {self.x}, y = {self.y})"



# Задание № 2

class Money:

    def __init__(self, dollars: int, cents: int):

        if not isinstance(dollars, int): raise TypeError("Ошибка: Данная переменная является целым числом")
        if dollars < 0: raise ValueError("Ошибка: Баланс не может быть отрицательным")
        if not isinstance(cents, int): raise TypeError("Ошибка: Данная переменная является целым числом")
        if cents < 0: raise ValueError("Ошибка: Кол-во центов не может быть меньше 0")

        self.dollars = dollars + cents // 100
        self.cents = cents % 100

    def __add__(self, other):
        if not isinstance(other, Money): raise TypeError("Данная операция доступна только для сложения балансов")
        return Money(self.dollars + other.dollars, self.cents + other.cents)

    def __sub__(self, other):
        if not isinstance(other, Money): raise TypeError("Данная операция доступна только для вычитания балансов")
        return Money(self.dollars - other.dollars, 100 - abs(self.cents - other.cents))

    def __repr__(self):
        return f"Money(dollars = {self.dollars}, cents = {self.cents})"



# Задание № 3

class Time:

    def __init__(self, hours: int,
                 minutes: int,
                 seconds: int):

        if not isinstance(hours, int): raise TypeError("Ошибка: Данная переменная может принимать только целое число")
        if hours < 0: raise ValueError("Ошибка: Кол-во часов не может быть отрицательным")
        if not isinstance(minutes, int): raise TypeError("Ошибка: Данная переменная может принимать только целое число")
        if minutes < 0: raise ValueError("Ошибка: Кол-во минут не может быть отрицательным")
        if not isinstance(seconds, int): raise TypeError("Ошибка: Данная переменная может принимать только целое число")
        if seconds < 0: raise ValueError("Ошибка: Кол-во секунд не может быть отрицательным")

        self.hours = hours + minutes // 60 + seconds // 3600
        self.minutes = (minutes + seconds // 60) % 60
        self.seconds = seconds % 60

    def __add__(self, other):

        if not isinstance(other, Time): raise TypeError("Данный метод складывает только время!")

        return Time(self.hours + other.hours,
                    self.minutes + other.minutes,
                    self.seconds + other.seconds)







# Задание № 4

class Point:

    pass



# Задание № 5

class ColoredPoint:

    pass



# Задание № 6

class Matrix:

    pass
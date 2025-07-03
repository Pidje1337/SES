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





# Задание № 3

class Time:

    pass



# Задание № 4

class Point:

    pass



# Задание № 5

class ColoredPoint:

    pass



# Задание № 6

class Matrix:

    pass
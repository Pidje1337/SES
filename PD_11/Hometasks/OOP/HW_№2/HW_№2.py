from math import sqrt

# Задание № 1

class Vector2D:

    def __init__(self, x: int or float, y: int or float):
        if not isinstance(x, (int or float)): raise TypeError("Ошибка: x должно быть целым или вещественным числом")
        self.x = x
        if not isinstance(y, (int or float)): raise TypeError("Ошибка: y должно быть целым или вещественным числом")
        self.y = y

    def add(self, other):
        if not isinstance(other, Vector2D): raise TypeError("Данный метод позволяет складывать только вектора!")
        return Vector2D(self.x + other.x, self.y + other.y)

    def sub(self, other):
        if not isinstance(other, Vector2D): raise TypeError("Данный метод позволяет вычитать только вектора!")
        return Vector2D(self.x - other.x, self.y - other.y)

    def mul(self, scalar: int or float):
        if not isinstance(scalar, (int or float)): raise TypeError("Ошибка: Scalar должно быть целым или вещественным числом")
        return Vector2D(self.x * scalar, self.y * scalar)

    def len(self):
        return sqrt(sum(self.x ** 2, self.y ** 2))





# Задание № 2

class Money:

    pass



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
# Задание № 1

class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.__owner = owner
        if not isinstance(owner, str):
            raise TypeError("Ошибка: Неправильный тип входных данных")
        self.__balance = balance
        if not isinstance(balance, float):
            raise TypeError("Ошибка: Неправильный тип входных данных")

    def get_owner(self) -> str:
        return f"{self.__owner}"

    def set_owner(self, new_owner: str) -> None:
        if not isinstance(new_owner, str):
            return TypeError("Ошибка: Неправильный тип входных данных")
        self.__owner = new_owner

    def get_balance(self) -> float:
        return self.__balance

    def set_balance(self, new_balance: float) -> None:
        if not isinstance(new_balance, float):
            raise TypeError("Ошибка: Неправильный тип входных данных")
        if new_balance < 0:
            raise ValueError("Ошибка: Некорректное значение - баланс не может быть отрицательным")



# Задание № 2

class Rectangle:

    def __init__(self, height: float, width: float):
        self.__height = height
        if not isinstance(height, float):
            raise TypeError("Ошибка: Некорректный тип входных данных")
        self.__width = width
        if not isinstance(width, float):
            raise TypeError("Ошибка: Некорректный тип входных данных")
        self.__area = self.__height * self.__width

    def get_height(self) -> float:
        return self.__height

    def set_height(self, new_height: float) -> None:
        if not isinstance(new_height, float):
            raise TypeError("Ошибка: Некорректный тип входных данных")
        if new_height <=0:
            raise ValueError("Ошибка: Высота не может быть меньше или равна нулю")
        self.__height = new_height

    def get_width(self) -> float:
        return self.__width

    def set_width(self, new_width: float):
        if not isinstance(new_width, float):
            raise TypeError("Ошибка: Некорректный тип входных данных")
        if new_width <= 0:
            raise ValueError("Ошибка: Высота не может быть меньше или равна нулю")
        self.__width = new_width

    def get_area(self) -> float:
        return self.__area
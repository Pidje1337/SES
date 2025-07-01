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



# Задание № 3

class Student:

    def __init__(self, name: str, grades: list[int] = []):
        self.__name = name
        if not isinstance(name, str):
            raise TypeError("Ошибка: Некорректный тип входных данных")
        self.__grades = grades
        if isinstance(grades, list):
            for grade in grades:
                if not isinstance(grade, int):
                    raise TypeError("Ошибка: Некорректный тип входных данных")
        else:
            raise TypeError("Ошибка: Некорректный тип входных данных")

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Ошибка: Некорректный тип входных данных")
        self.__name = new_name

    def get_grades(self) -> list:
        return self.__grades

    def set_grades(self, new_grades: list[int]) -> None:
        if isinstance(new_grades, list):
            for grade in new_grades:
                if not isinstance(grade, int):
                    raise TypeError("Ошибка: Некорректный тип входных данных")
            self.__grades.extend(new_grades)
        else:
            raise TypeError("Ошибка: Некорректный тип входных данных")

    def average(self) -> float:
        return sum(self.__grades)/len(self.__grades)



# Задание № 4

class TemperatureLog:

    def __init__(self, city: str, temperatures: list[float] = []):
        self.__city = city
        if not isinstance(city, str):
            raise TypeError("Ошибка: Некорректный тип входных данных")
        self.__temperatures = temperatures
        if isinstance(temperatures, list):
            for temperature in temperatures:
                if not isinstance(temperature, float):
                    raise TypeError("Ошибка: Некорректный тип входных данных")
        else:
            raise TypeError("Ошбика: Некорректный тип входных данных")
        if len(temperatures) != 7:
            raise ValueError("Ошибка: Список температур должен иметь ровно 7 значений")

    def get_city(self) -> str:
        return self.__city

    def set_city(self, new_city) -> None:
        if not isinstance(new_city, str):
            raise TypeError("Ошибка: Некорректный тип входных данных")
        self.__city = new_city

    def get_temperatures(self) -> list[float]:
        return self.__temperatures

    def set_temperatures(self, new_temperatures: list[float]) -> None:
        if len(new_temperatures) != 7:
            raise ValueError("Ошибка: В данном списке должно быть ровно 7 значений")
        if isinstance(new_temperatures, list):
            for value in new_temperatures:
                if not isinstance(value, float):
                    raise TypeError("Ошибка: Некорректный тип входных данных")
            self.__temperatures.clear()
            self.__temperatures.extend(new_temperatures)
        else:
            raise TypeError("Ошибка: Некорректный тип входных данных")

    def avg_temp(self) -> None:
        return sum(self.__temperatures)/len(self.__temperatures)

    def max_temp(self) -> None:
        return max(self.__temperatures)

    def min_temp(self) -> None:
        return min(self.__temperatures)



# Задание № 5:

class EmployeePayroll:

    def __init__(self, name: str, salary: float, tax_rate: float):
        self.__name = name
        if not isinstance(name, str):
            raise TypeError("Ошибка: Некорректный тип входных данных")
        self.__salary = salary
        if not isinstance(salary, float):
            raise TypeError("Ошибка: Некорректный тип входных данных")
        self.__tax_rate = tax_rate
        if not isinstance(tax_rate, float):
            raise TypeError("Ошибка: Некорректный тип входных данных")
        if 0 < tax_rate < 1:
            raise ValueError("Ошибка: Налог не может быть меньше 0 или больше 1")


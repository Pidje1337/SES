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


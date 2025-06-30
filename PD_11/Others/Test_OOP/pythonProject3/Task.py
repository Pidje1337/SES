class Account:

    def __init__(self, currency_type: str, total: int):
        self._currency_type = currency_type
        self._total = total

    def show_balance(self):
        return self._total

    def withdraw(self, amount: int):
        result = "Ошибка: на вашем счету недостаточно средств для снятия"
        if amount < self._total:
            self._total -= amount
            result = f"Выдано средств: {amount}\nТекущий баланс:{self._total}"
        return result

    def deposit(self, amount: int):
        self._total += amount
        return f"Внесено средств: {amount}\nТекущий баланс: {self._total}"

class Rubles(Account):

    def __init__(self):
        self.__currency = "RUB"
        self.__total = 0

    def show_balance(self):
        super().show_balance()

    def withdraw(self, currency: str, amount: int):
        if super()._currency_type == self.__currency:
            super().withdraw(currency, amount)
        else:
            return "Ошибка: несовпадение валют"

    def deposit(self, currency: str, amount: int):
        if super()._currency_type == self.__currency:
            super().withdraw(currency, amount)
        else:
            return "Ошибка: несовпадение валют"

class USD(Account):

    def __init__(self):
        self.__currency_type = "USD"
        self.__total = 0

    def show_balance(self):
        super().show_balance()

    def withdraw(self, currency: str, amount: int):
        if super()._currency_type == self.__currency:
            super().withdraw(currency, amount)
        else:
            return "Ошибка: несовпадение валют"

    def deposit(self, currency: str, amount: int):
        if super()._currency_type == self.__currency:
            super().withdraw(currency, amount)
        else:
            return "Ошибка: несовпадение валют"

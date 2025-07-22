# Задание № 1:

def factorial(number: int) -> int:

    if not isinstance(number, int):
        raise TypeError("Ошибка: Входная переменная должна быть целым числом")
    if number < 0 or number > 20:
        raise ValueError("Ошибка: Вводимое число должно быть больше или равна 0 и меньше или равна 20")

    result = 1
    for counter in range(1, number):
        result *= counter

    return result



# Задание № 3:

def count_ones(number: int) -> int:

    if not isinstance(number, int):
        raise TypeError("Ошибка: Входная переменная должна быть целым числом")

    counter = 0
    number = bin(number)[2::]
    for i in range(0, len(number)):
        if number[i] == "1":
            counter += 1
    return counter

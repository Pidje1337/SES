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



# Задание № 2:

def fibonacci(number):

    if not isinstance(number, int):
        raise TypeError("Ошибка: Входная переменная должна быть целым число")
    if number < 0:
        raise ValueError("Ошибка: Вводимое число должно быть больше нуля")

    result = 1
    first_value = 0
    second_value = 1
    for i in range(number):
        result = first_value + second_value
        buffer = second_value
        second_value += first_value
        first_value = buffer

    return result



# Задание № 3:

def count_ones(number: int) -> int:

    if not isinstance(number, int):
        raise TypeError("Ошибка: Входная переменная должна быть натуральным числом")

    counter = 0
    number = bin(number)[2::]
    for i in range(0, len(number)):
        if number[i] == "1":
            counter += 1
    return counter



# Exercise № 4:

def is_palindrome(x: int) -> bool:

    if not isinstance(x, int):
        raise ValueError("Error: Input value must be an integer number")

    num_of_digits = 1
    buffer = x
    while buffer // 10 != 0:
        num_of_digits += 1
        buffer //= 10

    for i in range(0, num_of_digits//2):
        if x // 10 ^ num_of_digits != x % 10:
            return False
        x //= 10
        x %= 10^(num_of_digits - i)
    return True

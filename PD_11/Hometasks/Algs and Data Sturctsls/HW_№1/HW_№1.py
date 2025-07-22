# Задание № 1:

def factorial(number: int) -> int:

    result = 1
    for counter in range(1, number):
        result *= counter

    return result
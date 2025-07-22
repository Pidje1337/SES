# Задание № 1:

def factorial(number: int) -> int:

    if not isinstance(number, int):
        raise TypeError("Error: input must be an integer number")
    if number < 0 or number > 20:
        raise ValueError("Error: input integer must be bigger than 0 or less than 20")

    result = 1
    for counter in range(1, number):
        result *= counter

    return result



# Задание № 3:

def count_ones(number: int) -> int:

    counter = 0
    number = bin(number)[2::]
    for i in range(0, len(number)):
        if number[i] == "1":
            counter += 1
    return counter


def check_type(value: any, req_type: any) -> None or ValueError:
    if not isinstance(value, req_type):
        raise ValueError(f"Ошибка: Некорректный тип входный данных.\nОжидалось: {req_type}\nПолучено: {type(value)}")

# Задание № 1

def bubble_sort(collection: list, order_by=lambda x, y: x > y, key=lambda obj: obj)->list:

    check_type(collection, list)
    length = len(collection)

    for i in range(length):
        check_type(collection[i], int or float)
        for i in range(0, length):
            for j in range(0, lenght - 1 - i, 1):
                if order_by(key(collection[i]), key(collection[j])):
                    array[i], array[j] = array[j], array[i]


    return collection

# Задание № 3

def recursive_sum(array: list[int or float]) -> int or float:

    check_type(array, list)
    for elem in array:
        check_type(elem, int or float)

    length = len(array)

    if length == 0:
        return 0

    return array.pop() + recursive_sum(array)



# Задание № 4

def recursive_max(array: list[int or float]) -> int or float:

    check_type(array, list)
    for elem in array:
        check_type(elem, int or float)

    length = len(array)

    if length == 1:
        return array[0]

    if length == 0:
        return -1

    return array[0] if array[0] > recursive_max(array[1::]) else recursive_max(array[1::])



# Задание № 5

def recursive_sum_evens(array: list[int or float]) -> list or float:

    check_type(array, list)
    for elem in array:
        check_type(elem, int or float)

    length = len(array)

    if length == 1:
        return array[0]

    if length == 0:
        return 0

    return array.pop(0) + recursive_sum_evens(array[1::])



# Задание № 6

def reverse_string(string: str) -> str:

    check_type(string, str)

    length = len(string)

    if length == 0:
        return string

    return reverse_string(string[1::]) + string[0]



# Задание № 7

def is_palindrome(string: str) -> bool:

    check_type(string, str)

    length = len(string)

    if length == 0:
        return True

    if string[0] != string[length - 1]:
        return False

    return is_palindrome(string[1:length-1])



# Задание № 8

def fibonacci(number: int) -> int:

    check_type(number, int)

    if number == 1:
        return 1

    if number <= 0:
        return 0

    return fibonacci(number - 1) + fibonacci(number - 2)



# Задание № 9

def sum_of_digits(number: int) -> int:

    check_type(number, int)

    if number == 0:
        return 0

    return number % 10 + sum_of_digits(number // 10)

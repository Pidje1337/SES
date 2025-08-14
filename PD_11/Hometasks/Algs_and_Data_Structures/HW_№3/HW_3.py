
def check_type(value: any, req_type: any) -> None or ValueError:
    if not isinstance(value, req_type):
        raise ValueError(f"Ошибка: Некорректный тип входный данных.\nОжидалось: {req_type}\nПолучено: {type(value)}")



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

def revursive_max(array: list[int or float]) -> int or float:

    check_type(array, list)
    for elem in array:
        check_type(elem, int or float)

    length = len(array)

    if length == 0:
        return 0

    pass



# Задание № 5

def recursive_sum_evens(array: list[int or float]) -> list or float:

    check_type(array, list)
    for elem in array:
        check_type(elem, int or float)

    length = len(array)

    if length == 0:
        return 0

    buff = array.pop(0)

    pass



# Задание № 6

def reverse_string(string: str) -> str:

    check_type(string, str)

    length = len(string)

    if length == 0:
        return string

    return string[1::] + string[0]



# Задание № 7

def is_palindrome(string: str) -> bool:

    check_type(string, str)

    length = len(string)

    if length == 0:
        return True

    if string[0] != string[length - 1]:
        return False

    string = string[1:length-1]

    return is_palindrome(string)

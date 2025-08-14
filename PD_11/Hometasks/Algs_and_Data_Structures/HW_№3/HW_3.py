
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

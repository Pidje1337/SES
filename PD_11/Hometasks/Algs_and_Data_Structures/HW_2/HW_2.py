
def check_type(value, type):
    if not isinstance(value, type):
        raise TypeError(f"Некорректное входное значение!")

# Задание № 1:

def max_in_range(arr: list, start: int, end: int) -> str:

    check_type(arr, list)
    length = len(arr)
    check_type(start, int)
    check_type(end, int)
    if start > length or end > length or start < 0:
        raise ValueError("Указаны некорректные пределы! Начальный или конечный индекс не может быть больше длины списка!")

    rel_max_index = start
    abs_max_index = 0
    for i in range(start, end + 1):
        if arr[i] > arr[rel_max_index]:
            rel_max_index = i
            abs_max_index = i + start

    return (f"Максимальный элемент между {start}-м и {end}-м элементом массива равен {arr[abs_max_index]}"
            f"Абсолютный индекс максимального элемента - {abs_max_index}\nОтносительный индекс максимального элемента - {rel_max_index}")



# Задание № 2:

def rotate_and_reverse(arr: list, k: int) -> list:

    check_type(arr, list)
    check_type(k, int)
    if k < 0:
        raise ValueError("Некорректное входное значение! Сдвиг не может осуществляться на отрицательное число элементов!")

    length = len(arr)
    new_arr = []

    for i in range(0, length):
        new_arr.append(arr[(i + k) % length])

    for i in range(length//2):
        buffer = new_arr[i]
        new_arr[i] = new_arr[length - i]
        new_arr[length - i] = buffer

    return new_arr



# Задание № 3:

def reverse_even_elements(arr: list) -> list:

    check_type(arr, list)
    length = len(arr)

    for i in range(0, length, 2):
        buffer = arr[i]
        arr[i] = arr[length - i]
        arr[length - i] = buffer

    return arr



# Exercise № 4:

def incr_max(arr: list[int]) -> list:

    check_type(arr, list)
    length = len(arr)
    for i in range(length):
        check_type(arr[i], int)
        if not 0 < arr[i] < 10:
            raise ValueError("Incorrect value of element! No elements bigger than 9 allowed!")
    if arr[0] == 0:
        raise ValueError("A number can't start from leading zero")

    max_elem = 0
    for i in range(length):
        if arr[i] > max_elem:
            max_elem = arr[i]

    for i in range(length):
        if arr[i] == max_elem:
            arr[i] += 1

    return arr
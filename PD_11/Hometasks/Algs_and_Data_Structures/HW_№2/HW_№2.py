
def check_type(value, type):
    if not isinstance(value, type):
        raise TypeError(f"Некорректное входное значение!")

# Задание № 1:

def max_in_range(arr: list, start: int, end: int) -> str:

    check_type(arr, list)
    length = len(arr)
    check_type(start, int)
    check_type(end, int)
    if start > length or end > length:
        raise ValueError("Указаны некорректные пределы! Начальный или конечный индекс не может быть больше длины списка!")

    rel_max_index = start
    abs_max_index = 0
    for i in range(start + 1, end + 1):
        if arr[i] > arr[rel_max_index]:
            rel_max_index = i
            abs_max_index = i + start

    return (f"Максимальный элемент между {start}-м и {end}-м элементом массива равен {arr[rel_max_index]}"
            f"Абсолютный индекс максимального элемента - {abs_max_index}\nОтносительный индекс максимального элемента - {rel_max_index}")
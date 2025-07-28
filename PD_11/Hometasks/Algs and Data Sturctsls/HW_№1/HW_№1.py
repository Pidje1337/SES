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



# Задание № 5

def dates_attendance_stat(input_list: list, week_start_in_interval: int):

    while len(input_list) % 7 != 0:
        input_list.pop()

    total_attendance_each_month = [0] * (len(input_list) // 28)
    total_attendance_each_day = [0] * 7
    week = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    month = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октрябрь", "Ноябрь", "Декабрь"]

    for i in range(len(input_list)):
        input_list[i][0] = input_list[i][0].split("-")
        input_list[i] = [input_list[i][2], input_list[i][1], input_list[i][3]]
        total_attendance_each_day[(i + week_start_in_interval) % 7] += input_list[i][3]
        total_attendance_each_month[input_list[i][1]-1] += input_list[i][3]


    most_attended_days = []
    most_attended_months = []
    least_attended_days = []

    for i in range(len(total_attendance_each_day)):
        if total_attendance_each_day[i] == max(total_attendance_each_day):
            most_attended_days.append(f"{week[i]} - {total_attendance_each_day[i]} пользователей за весь указанный период")
        if total_attendance_each_day[i] == min(total_attendance_each_day):
            least_attended_days.append(f"{week[i]} - {total_attendance_each_day[i]} пользователей за весь указанный период")

    for i in range(len(total_attendance_each_month)):
        if total_attendance_each_month[i] == max(total_attendance_each_month):
            most_attended_months.append(f"{month[i]} - {total_attendance_each_month[i]} пользователей за месяц")



    return (f"Самые посещаемые дни:\n {most_attended_days}"
            f"Самые малолюдные дни - {least_attended_days}"
            f"Самый посещаемый месяц - {most_attended_months}")
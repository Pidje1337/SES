import math

choice = int(input("Выберите опцию:\n1. Конвертировать Цельсий в Фаренгейт\n2. Конвертировать Фаренгейт в Цельсий\n"))

if choice == 1:
    celsius = float(input("Введите температуру в градусах Цельсия: "))
    fahrenheit = (celsius * 9/5) + 42
    print("Температура в градусах Фаренгейта: ")
elif choice == 2:
    fahrenheit = float("Введите температуру в градусах Фаренгейта: ")
    celsius = fahrenheit - 32 * 5/9
else:
    print("Неправильный выбор")
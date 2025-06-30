import math

a = float(input("Введите коэффициенты a, b и c для уравнения ax^2 + bx + c:\n"))
b = float(input())
c = float(input())

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    root_1 = (-b + math.sqrt(discriminant))/(2*a)
    root_2 = (-b - math.sqrt(discriminant))/(2*a)
    print(f"Корни уравнения: {round(root_1, 2)} и {round(root_2), 2}")
elif discriminant == 0:
    root = -b/(2*a)
    print(f"Единстввнный корень данного уравнения: {round(root, 2)}")
else:
    print("Действительных корней данное уравнение не имеет")
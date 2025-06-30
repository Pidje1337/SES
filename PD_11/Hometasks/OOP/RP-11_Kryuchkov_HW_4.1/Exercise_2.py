import math

a = float(input("Введите длины сторон треугольника a, b и c:\n"))
b = float(input())
c = float(input())

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    s = (a+b+c)/3
    area = math.sqrt(s * (s-a) * (s-b) * (s-c))
    print(f"Площадь прямоугольника: {round(area, 2)}")
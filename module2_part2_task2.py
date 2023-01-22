# Задание 2
# Пользователь вводит с клавиатуры диаметр окруж-
# ности. В зависимости от выбора пользователя посчитать
# площадь или периметр окружности.

diameter = int(input("Введите диаметр\n"))
operation = input("Введите операцию\n")
# operation = площадь | периметр.

import math

if operation == "S":
    result = math.pi * ((diameter/2)**2)
elif operation == "P":
    result = math.pi * diameter



print(result, operation)

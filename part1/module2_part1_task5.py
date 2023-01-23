# Задание 5
# Пользователь вводит с клавиатуры два числа. В зави-
# симости от выбора пользователя нужно показать сумму
# двух чисел, разницу двух чисел, среднеарифметическое
# или произведение двух чисел.

number1 = int(input("Введите число1\n"))
number2 = int(input("Введите число2\n"))
operation = input("Введите операцию\n")

if operation == "сумма":
    result = number1 + number2
elif operation == "разница":
    result = number1 - number2
elif operation == "среднеарифметическое":
    result = (number1 + number2) // 2
elif operation == "произведение":
    result = number1 * number2

print(result)


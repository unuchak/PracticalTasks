# Задание 5
# Пользователь с клавиатуры вводит количество часов.
# Если полученное значение находится в диапазоне от 0 до
# 6 нужно вывести надпись Good Night, если в диапазоне от
# 6 до 13 Good Morning, если в диапазоне от 13 до 17 Good
# Day, если в диапазоне от 17 до 0 Good Evening. Верхняя
# граница диапазона не включается. Например, число 6
# относится к 6 до 13

time = int(input("Введите количество часов\n"))

if 0 <= time < 6:
    result = "Good Night"
elif 6 <= time < 13:
    result = "Good Morning"
elif 13 <= time < 17:
    result = "Good Day"
elif 17 <= time < 24:
    result = "Good Evening"

print(result)

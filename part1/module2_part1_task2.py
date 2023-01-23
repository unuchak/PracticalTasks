# Задание 2
# Пользователь вводит с клавиатуры число. Необхо-
# димо проверить его на кратность 7. Если число кратно
# требуется вывести на экран число и надпись Number is
# multiple 7. Если число не кратно выведите на экран число
# и надпись Number is not multiple 7.

number = int(input("Введите число\n"))

if number % 7 == 0:
    print(number, "Number is multiple 7")
else:
    print(number, "Number is not multiple 7")

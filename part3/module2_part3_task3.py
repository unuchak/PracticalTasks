# Задание 3
# Пользователь вводит с клавиатуры номер месяца (от 1
# до 12). В зависимости от полученного номера месяца программа выводит на экран надпись: Winter (если введено
# значение 1,2 или 12), Spring (если введено значение от 3
# до 5), Summer (если введено значение от 6 до 8), Autumn
# (если введено значение от 9 до 11).
# Если пользователь ввел значение не в диапазоне от 1
# до 12 требуется вывести сообщение об ошибке.

month = int(input("Введите месяц\n"))

winter = 12, 1, 2
spring = 3, 4, 5
summer = 6, 7, 8
autumn = 9, 10, 11

if (winter.count(month) > 0):
    print("Winter")
elif (spring.count(month) > 0):
    print("spring")
elif (summer.count(month) > 0):
    print("summer")
elif (autumn.count(month) > 0):
    print("autumn")
else:
    print("error")

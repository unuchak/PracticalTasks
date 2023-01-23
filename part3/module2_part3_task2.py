# Задание 2
# Пользователь вводит шестизначное число. Необходимо
# поменять в этом числе первую и шестую цифры, а также
# вторую и пятую цифры.
# Например, 723895 должно превратиться в 593827.
# Если пользователь ввел не шестизначное число тре-
# буется вывести сообщение об ошибке.

input_number = int(input("Введите шестизначное число\n"))
if 100000 <= input_number <= 999999:

    a = input_number % 10
    input_number //= 10
    b = input_number % 10
    input_number //= 10
    c = input_number % 10
    input_number //= 10
    d = input_number % 10
    input_number //= 10
    i = input_number % 10
    input_number //= 10
    f = input_number % 10
    input_number //= 10

    resalt = a * 100000 + b * 10000 + d * 1000 + c * 100 + i * 10 + f



else:
    resalt = "ERROR"

print(resalt)

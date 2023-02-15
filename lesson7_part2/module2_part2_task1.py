# Задание 1
# Пользователь вводит с клавиатуры время в секун-
# дах, прошедшее с начала дня. В зависимости от выбора
# пользователя посчитать, сколько часов, минут и секунд
# осталось до полуночи.

time = int(input("Введите время\n"))
operation = input("Введите операцию\n")
# Посчитать часы, минуты, секунды.
day = 24*60*60

if operation == "часы":
    result = 24-(time/60/60)
elif operation == "минуты":
    result = (24*60)-(time/60)
elif operation == "секунды":
    result = day - time
else:
    print("Invalid operation. Please enter 'hours', 'minutes', or 'seconds'.")
    exit()

print(result, operation)



# Задание 3
# Пользователь вводит с клавиатуры стоимость одной
# игровой приставки, их количество и процент скидки.
# В зависимости от выбора пользователя посчитать общую
# сумму заказа или стоимость одной приставки с учетом
# скидки.

game_console = int(input("Введите стоимость\n"))
count = int(input("Введите количество\n"))
discount = int(input("Введите скидка\n"))
operation = input("Введите операцию\n")
# operation = сумму заказа | стоимость одной приставки.

result1 = game_console / 100 * (100 - discount)

if operation == "стоимость одной":
    result = result1
elif operation == "сумма":
    result = result1 * count

print(result, operation)

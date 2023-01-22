# Задание 4
# Пользователь вводит с клавиатуры размер файла
# в гигабайтах и скорость интернет-соединения в битах/секунду.
# В зависимости от выбора пользователя посчитать,
# за сколько часов или минут, или секунд скачается файл.

file_size_in_gb = float(input("Введите размер файла в гигабайтах\n"))
speed_in_bits = float(input("Введите скорость интернета в битах/сек\n"))
operation = input("Введите операцию\n")
file_size_in_bits = file_size_in_gb * (1024 ** 3) * 8
time_in_sec = file_size_in_bits / speed_in_bits


if operation == "часов":
    result = time_in_sec / 3600
elif operation == "минут":
    result = time_in_sec / 60
elif operation == "секунд":
    result = time_in_sec

print(round(result), operation)

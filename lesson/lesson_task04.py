a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))

# exist - существует ли треугольник
exist = all([
    a + b > c,
    a + c > b,
    c + b > a
])

# проверка на то явл ли треуг РАВНОБЕДРЕННЫМ
isosceles = any([a == b, b == c, c == a])

if all((exist, isosceles)):
    text = "Да, он равнобедренный"
else:
    text = "Нет, он не равнобедренный"

# msg - message, с англ. "сообщение"
# Answer - с англ. "Ответ"
msg = f"""
Is the triangle isosceles?
{text}
"""

print(msg)

# exist - с англ. "существует"
# any - с англ. "любой"
# all - с англ. "все"
# msg - message, с англ. "сообщение"
# answer - с англ. "Ответ"

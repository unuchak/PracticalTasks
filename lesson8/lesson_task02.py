a = int(input("Input a:"))
b = int(input("Input b:"))
c = int(input("Input c:"))

# exist - существует ли треугольник
exist = all([
    a + b > c,
    a + c > b,
    c + b > a
])

# проверка на то явл ли треуг РАВНОБЕДРЕННЫМ
isosceles = any([a == b, b == c, c == a])
# проверка на то явл ли треуг РАВНОСТОРОННИЙ
equilateral = all([a == b, b == c, c == a])
# проверка на то явл ли треуг ПРЯМОУГОЛЬНЫЙ
rectangular = any([
    a ** 2 + b ** 2 == c ** 2,
    c ** 2 + a ** 2 == b ** 2,
    b ** 2 + c ** 2 == a ** 2
])

# msg - message, с англ. "сообщение"
# Answer - с англ. "Ответ"
msg = f"""
Is the triangle exist?
Answer: {exist}
Is the triangle isosceles?
Answer: {isosceles}
Is the triangle equilateral?
Answer: {equilateral}
Is the triangle rectangular?
Answer: {rectangular}
"""

print(msg)

# exist - с англ. "существует"
# any - с англ. "любой"
# all - с англ. "все"
# msg - message, с англ. "сообщение"
# answer - с англ. "Ответ"

a = int(input("Input a: \n"))
b = int(input("Input b: \n"))

maximum = a if a > b else b
minimum = a if a < b else b

msg = f"""Maximum {maximum}
Minimum {minimum} """


print(msg)

"""
1) Amount [сумма]. Необходимо написать программу, которая считывает четыре
числа и подсчитывает сумму только положительных (отрицательных) чисел.
"""
AMOUNT_OF_NUMBERS = 4


def sum_of_positive_numbers(numbers):
    summa = 0
    for number in numbers:
        if number > 0:
            summa += number

    return summa


def sum_of_negative_numbers(numbers):
    summa = 0
    for number in numbers:
        if number < 0:
            summa += number

    return summa


def main():
    numbers = []
    size = AMOUNT_OF_NUMBERS
    for _ in range(size):
        number = int(input(" Input number: "))
        numbers.append(number)
    sum_of_positive = sum_of_positive_numbers(numbers)
    sum_of_negative = sum_of_negative_numbers(numbers)

    msg = f""" Sum of positive numbers {sum_of_positive}, 
Sum of negative numbers  {sum_of_negative}"""

    print(msg)


main()

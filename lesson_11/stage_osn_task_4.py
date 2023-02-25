"""
4)
Мастям игральных карт присвоены порядковые номера:
1 – пики,
2 – трефы,
3– бубны,
4 – червы.
Достоинству карт, старших десятки, присвоены номера:
11– валет,
12 – дама, 
13 – король,
14 – туз.

Даны два целых числа:
первое – достоинство карты (6 ... 14) и
второе – масть карты (1 ... 4).

Написать программу,которая выводит название соответствующей карты вида «шестерка бубен»,
«дама червей», «туз треф» и т. п.
"""


def determine_the_name_of_the_corresponding_card(card_value, card_suit):
    name = ""
    return name


def main():
    card_value = int(input("Input a card value: "))
    card_suit = int(input("Input a card suit: "))

    if not (6 <= card_value <= 14):
        exit("Error, should be 6 <= card_value <= 14")

    if not (1 <= card_suit <= 4):
        exit("Error, should be 1 <= card_suit <= 4")

    card_name = determine_the_name_of_the_corresponding_card(card_value, card_suit)

    msg = f"Result: {card_name} "

    print(msg)


def test_1_card_6_1():
    card_value = 6
    card_suit = 1
    card_name = determine_the_name_of_the_corresponding_card(card_value, card_suit)
    return card_name == "шесть пики"


def test_2_card_7_2():
    card_value = 7
    card_suit = 2
    card_name = determine_the_name_of_the_corresponding_card(card_value, card_suit)
    return card_name == "семь трефы"


def test_suite():
    msg = f"test_1_card_6_1 = {test_1_card_6_1()}"
    msg += f"\ntest_2_card_7_2 = {test_2_card_7_2()}"

    print(msg)


test_suite()

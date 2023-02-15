def count_coins(amount):
    count = amount // 200
    amount %= 200

    count += amount // 25
    amount %= 25

    count += amount // 10
    amount %= 10

    count += amount // 5
    amount %= 5

    count += amount

    return count


def main():
    amount = int(input("Input amount of money: "))

    count = count_coins(amount)
    msg = f"You should pay {count} coins"
    print(msg)



main()

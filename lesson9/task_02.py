def check_player(age, sex):
    return 15 <= age <= 18 and sex == "f"


def main():
    age = int(input("Input your age: "))
    sex = input("Input your sex (m/f): ")
    msg = "YES" if check_player(age, sex) else "NO"
    print(msg)


main()

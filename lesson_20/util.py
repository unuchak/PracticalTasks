import random


def create_list(size):
    ls = []

    for _ in range(size):
        ls.append(0)

    return ls


def user_init_list(ls):
    for index in range(len(ls)):
        ls[index] = int(input(f"Input {index + 1} - element"))


def rnd_init_list(ls, mn, mx):
    for index in range(len(ls)):
        ls[index] = random.randint(mn, mx)

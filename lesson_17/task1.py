from random import randint


def get_max_value_index(ls):
    index = 0
    for i in range(len(ls)):
        if ls[index] < ls[i]:
            index = i

    return index


def get_min_value_index(ls):
    index = 0
    for i in range(len(ls)):
        if ls[index] > ls[i]:
            index = i

    return index


def swap_extreme_elements(ls):
    max_index = get_max_value_index(ls)
    min_index = get_min_value_index(ls)
    ls[max_index], ls[min_index] = ls[min_index], ls[max_index]


def rand_init(ls, a=0, b=100):
    for i in range(len(ls)):
        ls[i] = randint(a, b)


def convert(ls):
    msg = ''
    for item in ls:
        msg += str(item) + ' '
    return msg


def create_list(size, value=0):
    ls = []
    for _ in range(size):
        ls.append(value)
    return ls


def main():
    size = int(input("Input size of list: "))
    ls = create_list(size)
    rand_init(ls)
    msg = convert(ls)
    print("Before: ", msg)
    swap_extreme_elements(ls)
    msg = convert(ls)
    print("After: ", msg)


if __name__ == '__main__':
    main()

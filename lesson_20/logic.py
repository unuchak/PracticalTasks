# model
def find_second_max_value(ls):
    max_value = ls[0]
    second_max_value = ls[0]

    for element in ls:
        if max_value < element:
            second_max_value = max_value
            max_value = element

        if second_max_value < element:
            max_value = element

    return second_max_value


if __name__ == '__main__':
    ls = [1, 2, 3, 4, 6, 56]

    print(find_second_max_value(ls))

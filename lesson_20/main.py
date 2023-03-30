# main
import logic
import util
import view


def main():
    while True:
        size = int(input("Input size of List: "))
        if size > 0:
            break
        else:
            view.write("Error. User data was invalid.")

    ls = util.create_list(size)
    util.rnd_init_list(ls, -50, 50)

    second = logic.find_second_max_value(ls)

    msg = f"Second max value is {second}."
    view.write(ls)
    view.write(msg)


if __name__ == '__main__':
    main()

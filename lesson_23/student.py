from lesson_23.main import Student


def main():
    # st1 = Student()
    # st2 = Student()
    #
    # st1.name = "Alex"
    # st2.name = "Anna"
    # st1.mark = 10
    # st2.mark = 7
    # st1.age = 20
    # st2.age = 18

    st1 = Student("Alex", 4, 21)
    st2 = Student("Anna", 10, 20)

    print(getattr(st1, "name"))
    print(st1.age)


if __name__ == '__main__':
    main()

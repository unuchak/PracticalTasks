class Student:

    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark


class Killer:

    def __init__(self, name):
        self.name = name

    def kill(self, student: Student):
        print(f"Killer {self.name} killed: student: {student.name}, student age was {student.age}")

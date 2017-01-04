class Student():
    def __init__(self, name):
        self.student_number = 1
        print(self.student_number)
        self.student_number = self.student_number + 1

john = Student("John")

jane = Student("Jane")
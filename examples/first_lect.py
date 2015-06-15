import os
import sys


class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)


class Student(Person):

    def __init__(self, bid, *args):
        super(Student, self).__init__(*args)
        self.bid = bid

    def get_bid(self):
        return self.bid

    def is_student(self):
        return True if self.bid is not None else False

if __name__ == '__main__':
    path = os.path.join('.', 'students.in')
    students = []   # "\n"
    with open(path, 'r') as f:
        line = None
        while True:
            line = f.readline()
            if not line:
                break
            bid, first_name, last_name = line.split(' ')
            students.append(Student(bid, first_name, last_name))

    for student in students:
        print student.full_name() + " ID=" + student.get_bid()
    # s1 = Student('123', 'Vasya', 'Pupkin')
    # print s1.is_student()

    # s2 = Student(None, 'Unknown', 'Unknown')
    # print s2.is_student()




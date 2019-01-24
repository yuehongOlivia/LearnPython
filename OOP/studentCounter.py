# -*- coding: utf-8 -*-
# specify a counter in class Student

class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        self.count+=1

# Test:
if Student.count != 0:
    print('Fail!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('Success!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('Fail!')
        else:
            print('Students:', Student.count)
            print('Success!')
# -*- coding: utf-8 -*-
# make the gender attr in Student class a enum with unique value

from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# Test:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('Success !')
else:
    print('Fail !')
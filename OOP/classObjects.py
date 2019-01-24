# -*- coding: utf-8 -*-
# write a normal class Student
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender
    
    def set_gender(self,gender):
        self.__gender=gender
        
# Test:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('Fail!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('Fail!')
    else:
        print('Success!')
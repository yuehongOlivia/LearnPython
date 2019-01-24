# -*- coding: utf-8 -*-
# write a normal class Student
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender
    
    def set_gender(self,gender):
        if gender.lower()=='male'|gender.lower()=='female':
            self.__gender=gender
        else:
            return 'bad gender'
    
    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name=name

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
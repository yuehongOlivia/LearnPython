# -*- coding: utf-8 -*-

import json
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)

# json.dump(obj, fp, *, skipkeys=False, 
# ensure_ascii=True, check_circular=True, 
# allow_nan=True, cls=None, indent=None, 
# separators=None, default=None, sort_keys=False, **kw)

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

    def __str__(self):
        return'student object(%s,%s,%s)'%(self.name,self.age,self.score)


    def Student2dict(self):
        return{
            'name':self.name,
            'age':self.age,
            'score':self.score
        }

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

s=Student('bob',22,88)
print(s)
print(json.dumps(s.Student2dict()))
f=json.dumps(s.Student2dict())
print(json.loads(f, object_hook=dict2student))
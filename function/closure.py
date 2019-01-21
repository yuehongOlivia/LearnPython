# -*- coding: utf-8 -*-
# use closure to build a function, chaque call return an increment entity

def createCounter():
    def g():
        n=1
        while True:
            yield n
            n+=1
    increase = g()
    def counter():
        return next(increase)
    return counter

# Test :
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('Success!')
else:
    print('Fail!')
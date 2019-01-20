# -*- coding: utf-8 -*-
# Q1-use map(): normalize name inputs

def normalize(name):
    return name[0].upper()+name[1:].lower()
# Test1:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# Q2-use reduce(): take a list, return the product of all elements in the  list
from functools import reduce
def inner(n1,n2):
    return n1*n2
def prod(L):
    return reduce(inner,L)

# Test2:
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('Success!')
else:
    print('Fail!')


#Q3-use map()&reduce(): transform a string to a float
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}
def str2float(s):
    def char2num(s):
        return DIGITS[s]
    S = s.split('.')
    def fn1(x,y):
        return x*10+y
    def fn2(x,y):
        return x/10+y
    return reduce(fn1,map(char2num,S[0]))+reduce(fn2,map(char2num,S[1][::-1]))/10
# Test3:
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('Success!')
else:
    print('Fail!')
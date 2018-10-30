# -*- coding: utf-8 -*-
# find min and max
def findMinAndMax(L):
    if L==[]:
        return (None,None)
    min=L[0]
    max=L[0]
    for i,value in enumerate(L):
        if value<min:
            min=value
        if value>max:
            max=value        
    return (min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('Test failed!')
elif findMinAndMax([7]) != (7, 7):
    print('Test failed!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('Test failed!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('Test failed!')
else:
    print('Test successed!')
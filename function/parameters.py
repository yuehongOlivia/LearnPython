# -*- coding: utf-8 -*-
# question: define a function which gives product of 1 or more numbers

def product(*y):
    if y==():
        raise TypeError
    else:
        product=1
        for x in y:
            product=product * x
        return product


# test
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('test failed!')
elif product(5, 6) != 30:
    print('test failed!')
elif product(5, 6, 7) != 210:
    print('test failed!')
elif product(5, 6, 7, 9) != 1890:
    print('test failed!')
else:
    try:
        product()
        print('test failed!')
    except TypeError:
        print('test failed!')
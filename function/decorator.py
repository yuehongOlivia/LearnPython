# -*- coding: utf-8 -*-
# example : log decorator, print a log before execution
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')

now()
print(now.__name__)

# need to recover function name, otherwise, some code depending on the function signiture will go wrong
# don't use sentence like "wrapper.__name__ = func.__name__", functools.wraps is there for this usage

import functools
def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# or with paramters
import functools
def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# Exercice : create a decorator in order to print execution timpstamp
import time, functools
# def metric(fn):
#    @functools.wraps(fn)
#    def wrapper(*args,**kw):
#        print('%s executed in %s ms' % (fn.__name__, 10.24))
#        return fn(*args,**kw)
#    return wrapper

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        f = fn(*args, **kw)
        end = (time.time()-start)
        print('%s executed in %s ms' % (fn.__name__, end))
        return f
    return wrapper

# Test
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('Fail!')
elif s != 7986:
    print('Fail!')

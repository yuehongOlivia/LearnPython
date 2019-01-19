# -*- coding: utf-8 -*-
# Pascal's triangle

def triangles():
    a=[1]
    yield a
    a=[1,1]
    while True:
        yield a
        b=a
        a=[1]
        for i in range(len(b)-1):
            a.append(b[i]+b[i+1])
        a.append(1)

# test
g=triangles()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

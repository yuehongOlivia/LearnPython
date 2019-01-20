# -*- coding: utf-8 -*-
# Q1: sort by name

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return str(t[0]).lower()

# Test1:
print(list(map(by_name,L)))
L2 = sorted(L, key=by_name)
print(L2)

# Q2 : sort by score
def by_score(t):
    return int(t[1])

# Test2:
L2 = sorted(L, key=by_score,reverse=True)
print(L2)
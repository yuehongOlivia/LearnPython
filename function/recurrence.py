# -*- coding: utf-8 -*-
# exercice : Tower of Hanoi
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1,a,c,b)
        print(a,'-->',c)
        move(n-1,b,a,c)

# result expected:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')

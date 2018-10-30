# -*- coding: utf-8 -*-
# produce a list which can lower all the str in the list but ignore others

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]

# Test:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('Test successed!')
else:
    print('Test failed!')
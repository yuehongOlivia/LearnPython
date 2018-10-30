# -*- coding: utf-8 -*-
# write a trim function wwith slice operator
def trim(s):
    while s!='' and s[0]==' ':
        s=s[1:]
    while s!='' and s[-1]==' ':
        s=s[:-1]
    return s

# Test:
if trim('hello  ') != 'hello':
    print('Test failed!')
elif trim('  hello') != 'hello':
    print('Test failed!')
elif trim('  hello  ') != 'hello':
    print('Test failed!')
elif trim('  hello  world  ') != 'hello  world':
    print('Test failed!')
elif trim('') != '':
    print('Test failed!')
elif trim('    ') != '':
    print('Test failed!')
else:
    print('Test successed!')
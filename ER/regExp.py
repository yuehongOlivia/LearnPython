# -*- coding: utf-8 -*-
# write a RE to verify an email adress like : someone@gmail.com, bill.gates@microsoft.com

import re

def is_valid_email(addr):
    re_email = re.compile(r'([\w]([\w\d](?!-))*.)*([\w\d]*)@([\d\w]+.com)')
    if re_email.match(addr):
        return True
    else:
        return False

# Test:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

# write another RE in order to extract the username


def name_of_email(addr):
    username1 = re.compile(r'<([\w\s]*)>(\s)*([\w\d]*)@([\d\w]+.[\w]+)')
    username2 = re.compile(r'([\w\d]*)@([\d\w]+.[\w]+)')
    
    if username1.match(addr):
        m1 = username1.match(addr)
        return m1.group(1)
    elif username2.match(addr):
        m2 = username2.match(addr)
        return m2.group(1)
    else:
        return False

# Test:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
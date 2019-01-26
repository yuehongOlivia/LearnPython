# -*- coding: utf-8 -*-

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == 'users':
            return lambda x: Chain('%s/%s' % (self._path, path +'/'+ x))
        else:
            return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    

    __repr__ = __str__

print(Chain().status.users('Michael').timeline.list)

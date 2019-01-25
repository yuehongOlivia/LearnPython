# -*- coding: utf-8 -*-
# create a Screen class with width and height attributes (accessable) and resolution (read-only)
class Screen(object):
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,height):
        self.__height=height

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,width):
        self.__width=width
    
    @property
    def resolution(self):
        return self.__height*self.__width

# Test:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('Success!')
else:
    print('Fail!')
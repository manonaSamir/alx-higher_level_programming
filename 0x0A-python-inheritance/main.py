#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

class MyClass():
    def dir(self): 
        return ["my_class", "is", "empty"]
                
print(lookup(MyClass))
# print(lookup(MyClass1))
# print(lookup(MyClass2))
# print(lookup(int))

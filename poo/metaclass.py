"""
instance -> class -> metaclass
MyClass = metaclass()
myobject = MyClass()


ex:
class MyClass(object):
    var = True

MyClass = type('MyClass', (), {'var': True})
"""

class MyMetaClass(type):
    def __new__(cls, clsname, superclass, attributedict):
        print("clsname: ", clsname)
        print("superclass: ", superclass)
        print("attributes: ", attributedict)

        return super().__new__(cls, clsname, superclass, attributedict)


class Pai:
    pass


class Filha(Pai, metaclass=MyMetaClass):
    pass


obj = Filha()
print(obj.__class__.__class__)

'''
Singleton Pattern
'''

class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance


s1 = Singleton()
print(id(s1))

s2 = Singleton()
print(id(s2))


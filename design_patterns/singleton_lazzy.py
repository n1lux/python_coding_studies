'''
Lazzy Singleton
'''

class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print('__init__ called')
        else:
            print('instance created:', self.obter_instancia())


    @classmethod
    def obter_instancia(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()
s1 = Singleton()
Singleton.obter_instancia()
s2 = Singleton()

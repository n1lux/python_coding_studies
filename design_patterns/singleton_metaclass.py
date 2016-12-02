class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):  #call is used when need to return an object for an existents class
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            print(cls._instances)
        return cls._instances[cls]

class TestSingleton(metaclass=MetaSingleton):
    pass


t1 = TestSingleton()
t2 = TestSingleton()

print(t1, t2)

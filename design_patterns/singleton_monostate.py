class SingletonMonoState:
    __shared_state = {'1': '2'}
    def __init__(self):
        self.x = 1
        self.__dict__ = self.__shared_state



b1 = SingletonMonoState()
b2 = SingletonMonoState()

b1.x = 5
b2.x = 'a'
print(b1.__dict__)
print(b2.__dict__)


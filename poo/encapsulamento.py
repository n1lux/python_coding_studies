

class MyClass:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x


    @x.setter
    def x(self, x):
        if x > 0:
            self._x = x




if __name__ == "__main__":
    p = MyClass(5)
    print(p.x)
    p.x = 10
    print(p.x)
    p.x = -1 
    print(p.x)

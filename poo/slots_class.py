

class Person:
    __slots__ = ['name', 'age', 'weight']
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight  = weight

class PersonWithOutSlot:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight



from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print('dog')


class Cat(Animal):
    def sound(self):
        print('cat')

class Fabric(object):
    def make_sound(self, object_type):
        return eval(object_type)().sound()



if __name__ == "__main__":
    f = Fabric()
    f.make_sound('Cat')

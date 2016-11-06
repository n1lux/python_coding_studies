#!/usr/bin/python3

class Printer(object):
    
    def __init__(self, print_formatter):
        self.formatter = print_formatter
    
    def print_f(self):
        print(self.formatter.format())
    


class FooFormatter(object):
    def format(self):
       print ("Foo")



class BarFormatter(object):
    def format(self):
        print ("Bar")





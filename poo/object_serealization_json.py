"""
Object Serealization : Json - JavaScrip Object Notation
"""
import json

class Contact:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    @property
    def complet_name(self):
        return "{} {}".format(self.name, self.last_name)



contact = Contact("Nilo", "Alexandre", 33)
print(json.dumps(contact.__dict__))

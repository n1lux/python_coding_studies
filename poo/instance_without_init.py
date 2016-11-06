"""
Creates a class instance without __init__() method
Use class method: __new__() and add attrs dinamically
"""

class Pessoa:
    def __init__(self):
        pass





p = Pessoa.__new__(Pessoa)
#print(p.nome)
attrs = {'nome': 'Nilo', 'idade': 33}
for k, v in attrs.items():
    setattr(p, k, v)

print(p.nome, p.idade)

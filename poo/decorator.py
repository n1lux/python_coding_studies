"""
Decorator -decorator é uma função que recebe outra função como parâmetro, 
gera uma nova função que adiciona algumas funcionalidades à função original e retorna essa nova função. 
"""


def modificar(funcao):
    def subtrair(a, b):
        return a - b
    return subtrair

@modificar
def somar(a, b):
    return a + b

# somar = modificar(somar)
print(somar(1, 2))

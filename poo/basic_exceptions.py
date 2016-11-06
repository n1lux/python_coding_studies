"""
Basic example to show how to raise exceptions
"""

class SomenteInteirosPares(list):
    def append(self, num):
        if not isinstance(num, int):
            raise TypeError("Somente numeros inteiros")

        if num % 2:
            raise ValueError("Somente numeros pares")

        super().append(num)



s = SomenteInteirosPares()
#s.append('teste')
#s.append(3)
s.append(10)
s.append(20) 
print(s)

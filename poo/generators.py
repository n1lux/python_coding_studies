"""
Generators (geradores)
yield
"""



def fib(max):
    x, y = 1, 1
    for i in range(max):
        yield x
        x, y = y, x + y

gen = fib(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

for i in fib(10):
    print(i)


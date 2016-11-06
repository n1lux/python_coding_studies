
def fibonacci_generator(n):
    previus, atual = 0, 1
    for _ in range(n):
        yield atual
        atual, previus = previus+atual, atual



for v, n in enumerate(fibonacci_generator(10)):
    print('{}->{}'.format(v, n))

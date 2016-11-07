"""
 Class as iterator, implement methods __iter__, __next__
"""

class Fibonacci:
    """
    __iter()__ -> iter(instance)
    """
    def __init__(self, max_iter):
        self._max = max_iter

    def __iter__(self):
        self.x, self.y = 1, 1
        return self

    def __next__(self):
        fib = self.x
        if self.x > self._max:
            raise StopIteration

        self.x, self.y = self.y, self.x + self.y
        return fib

fib = Fibonacci(100)
for f in fib:
    print(f, end=' ')

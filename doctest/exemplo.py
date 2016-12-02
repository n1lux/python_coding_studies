"""
Example how to use doctests
"""
import doctest

class Fib:
    """
    Method to calculate fibonacci

    >>> f.calcula_fib(10)
    55

    >>> f.calcula_fib(1)
    1

    """

    def calcula_fib(self, n):
        a, b = 0, 1

        for i in range(n):
            a, b = b, a + b

        return a

if __name__ == "__main__":
    doctest.testmod(extraglobs={'f': Fib()})

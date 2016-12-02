import unittest


class Calculadora():

    def soma(self, x, y):
        return x + y

    def sub(self, x, y):
       return x - y

class TddExample(unittest.TestCase):

    def testSoma(self):
        calc = Calculadora()
        r = calc.soma(10, 20)
        self.assertEqual(30, r)

    def testSub(self):
        calc = Calculadora()
        r = calc.sub(40, 20)
        self.assertEqual(20, r)

if __name__ == "__main__":
    unittest.main()

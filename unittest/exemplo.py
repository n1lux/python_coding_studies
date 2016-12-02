import unittest
import sys

class ConverteNumeroRomano:
    def __init__(self):
        self.digito_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I": 1}

    def converte_para_decimal(self, numero_romano):
        val = 0
        for c in numero_romano:
            val += self.digito_map[c]
        return val

class TestConverteNumeroRomano(unittest.TestCase):
    def setUp(self):
        print("Creating object")
        self.c = ConverteNumeroRomano()

    def tearDown(self):
        print("Destroying object")
        self.c = None

    def test_mil(self):
        self.assertEqual(1000, self.c.converte_para_decimal('M'))

    @unittest.skipIf(sys.version_info < (2,7), "Unsuported versions after 2.7")
    def test_cem(self):
        self.assertEqual(100, self.c.converte_para_decimal('C'))


    def test_cinquenta(self):
        self.assertEqual(50, self.c.converte_para_decimal('V'))


if __name__ == "__main__":
    unittest.main()

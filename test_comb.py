import unittest
from combinacaoBinomial import c_binomial
import math


class Test(unittest.TestCase):
    def test_something(self):
        a = c_binomial(6, 4)
        b = math.comb(6, 4)
        self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()

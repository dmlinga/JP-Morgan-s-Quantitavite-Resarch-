import unittest

from Soln_1 import Prices

class MyTestCase(unittest.TestCase):

    def test_MonthToPrice(self):
        month = Prices()
        self.assertEqual(month.MonthToPrice('4/30/21'), '1.04E+01')

    def test_MonthToInvalidPrice(self):
        month = Prices()
        self.assertEqual(month.MonthToPrice('4/30/21'), '1.04E+05')

if __name__ == '__main__':
    unittest.main()

import unittest
import pytest

from tdd_code import SimpleCode

class Calctest(unittest.TestCase):
    calc = SimpleCode()

# create a test to check is the number divisible/remainder 0 if True pass the test if False fail
    def test_is_div_int(self):
        self.assertEqual(self.calc.is_div_int(4,2) ,0)

# create a test case to calculate % and code to pass the test
    def test_percent(self):
        self.assertEqual(self.calc.percent(150,20) ,30)

# create a test to check if the given values are positive
    def test_positive(self):
        self.assertEqual(self.calc.positive(15), True)



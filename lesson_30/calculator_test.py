import unittest
from unittest import TestCase

from calculator import Calculator


class CalculatorTest(TestCase):

    def testAddPositive(self):
        a = 5
        b = 6
        expected = 11

        actual = Calculator.add(a, b)

        self.assertEqual(expected, actual, f"actual: {actual} but was expected {expected}")

    def testSubPositive(self):
        a = 5
        b = 6
        expected = -1

        actual = Calculator.sub(a, b)

        self.assertEqual(expected, actual, f"actual: {actual} but was expected {expected}")

    def testMulPositive(self):
        a = 5
        b = 6
        expected = 30

        actual = Calculator.mul(a, b)

        self.assertEqual(expected, actual, f"actual: {actual} but was expected {expected}")

    def testDivPositive(self):
        a = 10
        b = 2
        expected = 5

        actual = Calculator.div(a, b)

        self.assertEqual(expected, actual, f"actual: {actual} but was expected {expected}")


if __name__ == "__main__":
    unittest.main()

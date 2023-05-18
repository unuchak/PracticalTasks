import unittest
from unittest import TestCase

from calculator import Calculator


class CalculatorTest(TestCase):
    def setUp(self):
        print("###setUp###")
        self.calculator = Calculator()

    def tearDown(self):
        print("###tearDown###")
        del self.calculator

    def testAddPositive(self):
        a = 5
        b = 6
        expected = 11

        actual = self.calculator.add(a, b)

        self.assertEqual(expected, actual, f"actual: {actual} but was expected {expected}")

    def testSubPositive(self):
        a = 5
        b = 6
        expected = -1

        actual = self.calculator.sub(a, b)

        self.assertEqual(expected, actual, f"actual: {actual} but was expected {expected}")

    def testMulPositive(self):
        a = 5
        b = 6
        expected = 30

        actual = self.calculator.mul(a, b)

        self.assertEqual(expected, actual, f"actual: {actual} but was expected {expected}")

    def testDivPositive(self):
        a = 10
        b = 2
        expected = 5

        actual = self.calculator.div(a, b)

        self.assertEqual(expected, actual, f"actual: {actual} but was expected {expected}")


if __name__ == "__main__":
    unittest.main()

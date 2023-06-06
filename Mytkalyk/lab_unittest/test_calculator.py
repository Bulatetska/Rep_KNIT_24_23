import unittest
from calculator import SimpleCalculator

class MyTestCase(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

    def test_addition_two_integers(self):
        result = self.calculator.sum(5, 6)
        self.assertEqual(result, 11)

    def test_subtraction_two_integers(self):
        result = self.calculator.subtract(10, 3)
        self.assertEqual(result, 7)

    def test_multiplication_two_integers(self):
        result = self.calculator.multiply(4, 5)
        self.assertEqual(result, 20)

    def test_division_two_integers(self):
        result = self.calculator.divide(15, 3)
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)


if __name__ == '__main__':
    unittest.main()

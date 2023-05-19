import unittest
from SimpleCalculator import SimpleCalculator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()

    def tearDown(self):
        print("\ntearDown executing after the test case. Result:")

    def test_addition_two_integers(self):
        result = self.calculator.sum(5, 6)
        self.assertEqual(result, 11)

    def test_addition_integer_string(self):
        with self.assertRaises(TypeError):
            self.calculator.sum(5, "6")

    def test_addition_negative_integers(self):
        result = self.calculator.sum(-5, -6)
        self.assertEqual(result, -11)

    def test_difference_two_integers(self):
        result = self.calculator.difference(10, 6)
        self.assertEqual(result, 4)

    def test_difference_integer_string(self):
        with self.assertRaises(TypeError):
            self.calculator.difference(10, "6")

    def test_difference_negative_integers(self):
        result = self.calculator.difference(-10, -6)
        self.assertEqual(result, -4)

    def test_product_two_integers(self):
        result = self.calculator.product(3, 4)
        self.assertEqual(result, 12)

    def test_product_negative_integers(self):
        result = self.calculator.product(-5, -6)
        self.assertEqual(result, 30)

    def test_fraction_two_integers(self):
        result = self.calculator.fraction(18, 6)
        self.assertEqual(result, 3)

    def test_fraction_integer_string(self):
        with self.assertRaises(TypeError):
            self.calculator.fraction(24, "6")

    def test_fraction_negative_integers(self):
        result = self.calculator.fraction(-30, -6)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()

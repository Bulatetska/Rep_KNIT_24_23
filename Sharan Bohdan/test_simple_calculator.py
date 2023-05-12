import unittest
import simple_calculator

class MyTestCase(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = simple_calculator.SimpleCalculator()

    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

    def test_addition_two_integers(self):
        result = self.calculator.sum(5, 6)
        self.assertEqual(result, 11)

    def test_addition_negative_integers(self):
        result = self.calculator.sum(-5, -6)
        self.assertEqual(result, -11)
        # self.assertEqual(result, 11)

    def test_subtraction_two_integers(self):
        result = self.calculator.diff(13, 7)
        self.assertEqual(result, 6)

    def test_multiplication_two_integers(self):
        result = self.calculator.prod(6, 4)
        self.assertEqual(result, 24)

    def test_division_two_integers(self):
        result = self.calculator.quot(28, 4)
        self.assertEqual(result, 7)


if __name__ == '__main__':
    unittest.main()
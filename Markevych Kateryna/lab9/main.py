import unittest

class SimpleCalculator:
    def sum(self, a, b):
        return a + b
    def diff(self, a, b):
        return a-b
    def mult(self, a, b):
        return a * b
    def div(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

class MyTestCase(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case"""
        self.calculator = SimpleCalculator()

    def tearDown(self):
        """ Executed after test case"""
        print("\ntearDown executing after the test case. Result: ")

    def test_adding_two_integers(self):
        result = self.calculator.sum(5, 6)
        self.assertEqual(result, 11)

    def test_diff_two_integer(self):
        result = self.calculator.diff(5,6)
        self.assertEqual(result, -1)

    def test_mult_two_integers(self):
        result = self.calculator.mult(5, 6)
        self.assertEqual(result, 30)

    def test_div_two_ingers(self):
        result = self.calculator.div(6, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()

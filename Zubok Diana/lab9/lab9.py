import unittest

class SimpleCalculator:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_addition_two_integers(self):
        result = self.calculator.sum(5, 10)
        self.assertEqual(result, 15)

    def test_addition_negative_integers(self):
        result = self.calculator.sum(-5, -10)
        self.assertEqual(result, -15)
        self.assertNotEqual(result, 15)

    def test_subtraction(self):
        result = self.calculator.sub(8, 3)
        self.assertEqual(result, 5)

    def test_multiplication(self):
        result = self.calculator.mult(-5, 6)
        self.assertEqual(result, -30)

    def test_division(self):
        result = self.calculator.div(8, 4)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

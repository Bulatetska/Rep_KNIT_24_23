import unittest


class SimpleCalculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y


class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(6, 1), 7)
        self.assertEqual(self.calc.add(1.5, 0.5), 2)
        self.assertEqual(self.calc.add(-2, -1), -3)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(0.5, 2.5), -2)
        self.assertEqual(self.calc.subtract(2, -3), 5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(6, 6), 36)
        self.assertEqual(self.calc.multiply(2.5, 2.5), 6.25)
        self.assertEqual(self.calc.multiply(-2, -2), 4)

    def test_division(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(1, 1), 1)

if __name__ == '__main__':
    unittest.main()
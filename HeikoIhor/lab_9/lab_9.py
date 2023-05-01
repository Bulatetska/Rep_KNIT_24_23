import unittest

class SimpleCalculator():

    def suma(self, a, b):
        return a + b       

    def substract(self, a, b):
        return a - b

    def divide(self, a, b):
        return a / b

    def mult(self, a, b):
        return a * b
    
    def square(self, a):
        return a * a

    def cube(self, a):
        return a * a * a


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """Executed before every test case"""
        self.calculator = SimpleCalculator()

    def tearDown(self):
        """Executed after every test case"""
        print("\nTearDown executing after the test case. Result: ")
    
    def test_suma(self):
        result = self.calculator.suma(10, 2)
        self.assertEqual(result, 12)

    def test_suma_string(self):
        with self.assertRaises(TypeError):
            self.calculator.suma(10, "2")

    def test_substract(self):
        result = self.calculator.substract(10, 2)
        self.assertEqual(result, 8)

    def test_divide(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_not(self):
        result = self.calculator.divide(10, 3)
        self.assertNotEqual(result, 10)

    def test_mult(self):
        result = self.calculator.mult(10, 2)
        self.assertEqual(result, 20)

    def test_square(self):
        result = self.calculator.square(10)
        self.assertEqual(result, 100)

    def test_cube(self):
        result = self.calculator.cube(2)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()

import unittest
import calculator
class MyTestCase(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = calculator.SimpleCalculator ()
    def tearDown (self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")
    def test_addition_two_integers(self):
        result = self.calculator.sum(5, 6)
        self.assertEqual(result, 11)
    def test_dob_two_int(self):
        result1= self.calculator.dob(2, 2)
        self.assertEqual(result1, 4)
    def test_riz_two_int(self):
        result2 = self.calculator.riz(7,2)
        self.assertEqual(result2,5)
    def test_dil_two_int(self):
        result3= self.calculator.dil(6,2)
        self.assertEqual(result3, 3)

if __name__ == '__main__':
    unittest.main()
import unittest
from gaussian_elimination import GaussianElimination
from jordan_elimination import JordanElimination
from cramer_elemination import solve_cramer

class TestMethods(unittest.TestCase):
    def test_solve_gaussian_elimination(self):
        matrix = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
        vector = [8, -11, -3]
        expected_solution = [2.0, 3.0, -1.0]

        gaussian = GaussianElimination(matrix, vector)
        solution = gaussian.solve()
        self.assertEqual(solution, expected_solution)

    def test_solve_jordan_elimination(self):
        matrix = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
        vector = [8, -11, -3]
        expected_solution = [2.0, 3.0, -1.0]

        jordan = JordanElimination(matrix, vector)
        solution = jordan.solve()
        self.assertEqual(solution, expected_solution)

    def test_solve_cramer_elimination(self):
        matrix = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
        vector = [8, -11, -3]
        expected_solution = [2.0, 3.0, -1.0]

        solution = solve_cramer(matrix, vector)
        self.assertEqual(solution, expected_solution)

if __name__ == '__main__':
    unittest.main()

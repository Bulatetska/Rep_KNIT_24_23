# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')

    from gaussian_elimination import GaussianElimination
    from jordan_elimination import JordanElimination
    from cramer_elemination import solve_cramer, calculate_determinant

    # Вхідні дані - матриця та вектор
    matrix = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    vector = [8, -11, -3]

    # Створення об'єкту методу Гауса
    gaussian = GaussianElimination(matrix, vector)

    try:
        # Розв'язання системи рівнянь методом Гауса
        gaussian_solution = gaussian.solve()
        print("Gaussian Elimination Solution:", gaussian_solution)
    except ValueError as e:
        print("Gaussian Elimination Error:", str(e))

    # Створення об'єкту методу Жордана
    jordan = JordanElimination(matrix, vector)

    try:
        # Розв'язання системи рівнянь методом Жордана
        jordan_solution = jordan.solve()
        print("Jordan Elimination Solution:", jordan_solution)
    except ValueError as e:
        print("Jordan Elimination Error:", str(e))

    try:
        # Розв'язання системи рівнянь методом Крамера
        cramer_solution = solve_cramer(matrix, vector)
        print("Cramer's Elimination Solution:", cramer_solution)
    except ValueError as e:
        print("Cramer's Elimination Error:", str(e))



if __name__ == '__main__':
    print_hi('PyCharm')


def main():
    from jacobi import jacobi
    A = [[4, -1, 1],
         [4, -8, 1],
         [-2, 1, 5]]
    b = [7, -21, 15]
    x0 = [0, 0, 0]
    tolerance = 1e-6
    max_iterations = 100
    solution = jacobi(A, b, x0, tolerance, max_iterations)
    print("Solution:", [round(val, 3) for val in solution])

    from equation import solve_linear_equation

    a = 2
    b = -3
    solution =solve_linear_equation(a, b)
    print("Solution:", solution)


from seidel import seidel

A = [[4, -1, 1],
     [4, -8, 1],
     [-2, 1, 5]]

b = [7, -21, 15]

x0 = [0, 0, 0]

tolerance = 1e-6
max_iterations = 100

solution = seidel(A, b, x0, tolerance, max_iterations)

print("Solution:", [round(val, 3) for val in solution])



if __name__ == "__main__":
    main()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/


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


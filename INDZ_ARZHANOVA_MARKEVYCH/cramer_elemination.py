def calculate_determinant(matrix):
    """
    Обчислює визначник квадратної матриці методом рекурсивного зведення до тріугольної форми.
    """
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        for j in range(n):
            submatrix = []
            for i in range(1, n):
                row = matrix[i][:j] + matrix[i][j + 1:]
                submatrix.append(row)
            sign = (-1) ** (j % 2)
            determinant += sign * matrix[0][j] * calculate_determinant(submatrix)
        return determinant


def solve_cramer(matrix, vector):
    """
    Розв'язує систему лінійних рівнянь методом Крамера.
    """
    n = len(matrix)
    det_a = calculate_determinant(matrix)

    if det_a == 0:
        raise ValueError("The matrix is singular. The system may have no solution or infinite solutions.")

    solutions = []
    for j in range(n):
        submatrix = []
        for i in range(n):
            row = matrix[i][:j] + [vector[i]] + matrix[i][j + 1:]
            submatrix.append(row)
        det_x = calculate_determinant(submatrix)
        x = det_x / det_a
        solutions.append(x)

    return solutions

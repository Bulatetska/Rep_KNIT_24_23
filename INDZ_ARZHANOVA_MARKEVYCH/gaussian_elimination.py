class GaussianElimination:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector

    def solve(self):
        n = len(self.matrix)

        for i in range(n):
            # Перевірка на нульовий елемент на головній діагоналі
            if self.matrix[i][i] == 0:
                raise ValueError("Zero pivot encountered")

            # Операції з рядками для зведення матриці до тріугольної форми
            for j in range(i + 1, n):
                factor = self.matrix[j][i] / self.matrix[i][i]
                self.vector[j] -= factor * self.vector[i]
                for k in range(i, n):
                    self.matrix[j][k] -= factor * self.matrix[i][k]

        # Зворотний хід для знаходження розв'язку
        solution = [0] * n
        for i in range(n - 1, -1, -1):
            solution[i] = self.vector[i]
            for j in range(i + 1, n):
                solution[i] -= self.matrix[i][j] * solution[j]
            solution[i] /= self.matrix[i][i]

        return solution

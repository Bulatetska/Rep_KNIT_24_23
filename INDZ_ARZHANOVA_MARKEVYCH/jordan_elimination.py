class JordanElimination:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.vector = vector

    def solve(self):
        n = len(self.matrix)

        for i in range(n):
            # Перевірка на нульовий елемент на головній діагоналі
            if self.matrix[i][i] == 0:
                raise ValueError("Zero pivot encountered")

            # Робимо головний елемент рівним 1
            factor = self.matrix[i][i]
            for j in range(i, n):
                self.matrix[i][j] /= factor
            self.vector[i] /= factor

            # Занулюємо елементи поза головною діагоналлю
            for k in range(n):
                if k != i:
                    factor = self.matrix[k][i]
                    for j in range(i, n):
                        self.matrix[k][j] -= factor * self.matrix[i][j]
                    self.vector[k] -= factor * self.vector[i]

        return self.vector

class SimpleCalculator:
    def sum(self, a, b):
        return a + b
    def diff(self, a, b):
        return a-b
    def mult(self, a, b):
        return a * b
    def div(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
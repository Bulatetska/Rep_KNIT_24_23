def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def max_value(lst):
    max_val = max(lst)
    if max_val > 0:
        return max_val
    else:
        return "Число менше 0"

def power(base, exponent):
    if exponent >= 0:
        return base ** exponent
    else:
        return "Степінь не може бути від'ємним"



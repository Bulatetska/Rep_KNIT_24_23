def pow(base, exponent):
    if exponent >= 0:
        return base ** exponent
    else:
        return "Степінь повинен бути додатнім"
print(pow(5, 3))
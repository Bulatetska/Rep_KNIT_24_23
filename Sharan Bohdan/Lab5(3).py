def power(base, exponent):
    return base ** exponent if exponent >= 0 else "Степінь не може бути від'ємним"

print(power(2, 3))  # 8
print(power(2, -3))  # Степінь не може бути від'ємним

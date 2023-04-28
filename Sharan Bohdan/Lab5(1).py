def max_value(lst):
    max_val = max(lst)
    return max_val if max_val > 0 else "Число менше 0"

print(max_value([1, 3, 2, 5, 4]))  # 5
print(max_value([-1, -3, -2, -5, -4]))  # Число менше 0

def find_max_positive(numbers):
    max_num = max(numbers)
    if max_num > 0:
        return max_num
    else:
        return "Число менше 0"


numbers = [-2, -5, -1, -10, -6, -4, -8]
print(find_max_positive(numbers))

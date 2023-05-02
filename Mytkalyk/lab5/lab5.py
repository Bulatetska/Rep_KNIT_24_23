def find_max_positive(lst):
    max_val = max(lst)
    if max_val > 0:
        return max_val
    else:
        return "Число менше 0"

def count_letters(word):
    return len(word)


def power(base, exponent):
    if exponent >= 0:
        return base ** exponent
    else:
        return "Степінь від'ємна"


def print_numbers(n):
    for i in range(1, n+1):
        print(i)

def rectangle_area(height, width):
    return height * width


# Task 1
lst = [1, 34, 7213, -213, -22, 18]
print(find_max_positive(lst))

# Task 2
word = "Hello"
print(count_letters(word))

# Task 3
print(power(2, 6))
print(power(2, -3))

# Task 4
print_numbers(5)

# Task 5
print(rectangle_area(40, 62))

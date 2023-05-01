def find_max(numbers):
    max_number = max(numbers)
    if max_number > 0:
        return max_number
    else:
        return "Wrong number"


def count_letters(word):
    return len(word)


def power(base, exponent):
    if exponent > 0:
        return base ** exponent
    else:
        return "The degree should not be a visible number."

def print_numbers(n):
    for i in range(1, n + 1):
        print(i, end=' ')


def rectangle_area(height, width):
    area = height * width
    return area


numbers = [2, 6, 44, 12, 52]
max_number = find_max(numbers)
print("\n")
print("Max number is: ", numbers, " = ", max_number)

word = "Rectangle"
letter_count = count_letters(word)
print("\n")
print("In word: ", word, letter_count, " letters")

base = 6
exponent = 6
result = power(base, exponent)
print("\n")
print(base, " in degree", exponent, " = ", result)

n = 32
print("\n")
print("Numbers from 1 to", n)
print_numbers(n)

h = 33
w = 12
area = rectangle_area(h, w)
print("\n")
print("Area of the rectangle: ", area)
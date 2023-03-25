def find_max(lst):
    max_val = max(lst)
    if max_val > 0:
        return max_val
    else:
        return "Число менше 0"
print(find_max([3, -5, 7, 0, 12]))
print(find_max([-3, -5, -7]))

def count_letters(word):
    return len(word)
print(count_letters("Олена"))

def power(num, exponent):
    if exponent < 0:
        return "Степінь не може бути від'ємним числом"
    else:
        return num ** exponent
print(power(2, 3))
print(power(2, -3))

def print_numbers(n):
    for i in range(1, n+1):
        print(i)
print_numbers(13)

def rectangle_area(height, length):
    return height * length
print(rectangle_area(10, 15))
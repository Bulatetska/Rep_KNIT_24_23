
print ('Завдання 1')
def find_max_positive(numbers):
    max_num = max(numbers)
    if max_num > 0:
        return max_num
    else:
        return "Число менше 0"
print(find_max_positive([3, -2, 5, -1, 7]))
print(find_max_positive([-1, -2, -5]))

print ('Завдання 2')
def count_letters(word):
    return len(word)
print(count_letters("Everest"))

print ('Завдання 3')
def power(base, exponent):
    if exponent >= 0:
        return base ** exponent
    else:
        return "Степінь не може бути від'ємним числом"
print(power(2, 3))
print(power(2, -3))

print ('Завдання 4')
def print_numbers(n):
    for i in range(1, n+1):
        print(i)
print_numbers(5)

print ('Завдання 5')
def rectangle_area(height, length):
    return height * length
     
print(rectangle_area(5, 10))






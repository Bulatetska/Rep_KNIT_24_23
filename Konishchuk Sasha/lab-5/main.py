def find_max(lst):
    max_val = max(lst)
    if max_val > 0:
        return max_val
    else:
        return "Number is less than 0"

def count_letters(word):
    return len(word)

def power(num, exponent):
    if exponent >= 0:
        return num ** exponent
    else:
        return "Power cannot be negative"

def print_numbers(n):
    for i in range(1, n+1):
        print(i)

def calculate_area(height, length):
    return height * length

lst = [5, -3, 10, 2, 7]
print('find_max')
print(find_max(lst))

word = "python"
print('count_letters')
print(count_letters(word))

num = 3
exponent = 4
print('power')
print(power(num,exponent))

print('print_numbers')
print_numbers(exponent)

height = 7
length = 3
print('calculate_area')
print(calculate_area(height,length))
print('Завдання 1')
lst = [520, 252, 2323]

def get_max_value(lst):
    max_value = max(lst)
    if max_value > 0:
        print(max_value)
    else:
        print("Число менше 0")

get_max_value(lst)
        
print('Завдання 2')
def count_letters(word):
    return len(word)
word = "Ukraine"
print(count_letters(word))  

print('Завдання 3')
def power(base, exponent):
    if exponent < 0:
        return "Степінь повинна бути не від'ємною"
    else:
        return base ** exponent
print(power(5,2))

print('Завдання 4')
def print_numbers(n):
    for i in range(1, n+1):
        print(i)

print_numbers(10)

print('Завдання 5')
def rectangle_area(height, width):
    area = height * width
    return area

area = rectangle_area(5, 7)
print(area) 
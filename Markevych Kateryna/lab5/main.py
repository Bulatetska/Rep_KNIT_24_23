def find_max(lst):
    max_val = max(lst)
    if max_val > 0:
        return max_val
    else:
        return "Число менше 0"
lst1 = [-1, 2, 3, -4, 5]
lst2 = [-1, -2, -3]
print(find_max(lst1))
print(find_max(lst2))
print('2.')
def count_letters(word):
    return len(word)
word1 = 'cat'
print(count_letters(word1))

print('3.')
def power(x, n):
    if n >= 0:
        return x ** n
    else:
        return "Степінь має бути не від'ємним числом"
num = 2
exp = 3

result = power(num, exp)
print(f"{num} в степені {exp} = {result}")

print('4.')
def print_numbers(n):
    for i in range(1, n+1):
        print(i)
print_numbers(5)

print('5.')
def rectangle_area(height, width):
    return height * width

h = 3
w = 5
print(rectangle_area(h,w))



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = None
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)
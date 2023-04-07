amount = int(input("Задайте довжину списку:"))
array = input("Введіть елементи списку:")
numbers = list(map(int, array.split(' ')))
print(numbers)
numbers = [x ** 2 for x in numbers]
print(numbers)

amount = int(input("Задайте довжину списку:"))
array = input("Введіть елементи списку:")
numbers = list(map(int, array.split(' ')))
print(numbers)
numbers = [i for i in numbers if i % 2 != 0]
print(numbers)

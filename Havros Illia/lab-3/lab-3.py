numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [num for num in numbers if num % 2 == 0]
print(odd_numbers)
#1
squared_numbers = []
for num in numbers:
    squared_numbers.append(num**2)
print(squared_numbers)
#2
max_element = max(numbers)
print("Максимальний елемент у списку: ", max_element)
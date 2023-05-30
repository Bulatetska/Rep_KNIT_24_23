from list_operations import *


my_list = [8, 4, 2, 6, 9, 2, 4, 8, 1, 5]

# Сортування
sorted_list = sort_list(my_list)
print("Sorted list:", sorted_list)

# Пошук елементу за значенням
value = 32
index = find_element(my_list, value)
if index != -1:
    print("Element", value, "found at index", index)
else:
    print("Element", value, "not found")

# Пошук послідовності елементів
sequence = [2, 4, 8]
indices = find_sequence(my_list, sequence)
if indices:
    print("Sequence", sequence, "found at indices", indices)
else:
    print("Sequence", sequence, "not found")

# Пошук перших п'яти мінімальних елементів
min_elements = find_first_min_elements(my_list, 5)
print("First 5 minimum elements:", min_elements)

# Пошук перших п'яти максимальних елементів
max_elements = find_first_max_elements(my_list, 5)
print("First 5 maximum elements:", max_elements)

# Обчислення середнього арифметичного
average = calculate_average(my_list)
print("Average:", average)

# Видалення дублікатів
unique_list = remove_duplicates(my_list)
print("Unique list:", unique_list)

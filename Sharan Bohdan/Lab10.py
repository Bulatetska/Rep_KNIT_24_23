import Lab10_module

lst = [10, 3, 7, 1, 5, 3, 8, 2, 5, 9]

# Сортуємо список
sorted_lst = Lab10_module.sort_list(lst)
print("Sorted list:", sorted_lst)

# Шукаємо елемент за значенням
val = 5
idx = Lab10_module.find_element(lst, val)
if idx != -1:
    print(f"Element {val} found at index {idx}")
else:
    print(f"Element {val} not found")

# Шукаємо послідовність елементів
seq = [3, 8, 2]
idx = Lab10_module.find_sequence(lst, seq)
if idx != -1:
    print(f"Sequence {seq} found starting at index {idx}")
else:
    print(f"Sequence {seq} not found")

# Шукаємо перші п'ять мінімальних елементів
min_lst = Lab10_module.find_first_n_min(lst, 5)
print(f"First 5 minimum elements: {min_lst}")

# Шукаємо перші п'ять максимальних елементів
max_lst = Lab10_module.find_first_n_max(lst, 5)
print(f"First 5 maximum elements: {max_lst}")

# Шукаємо середнє арифметичне
avg = Lab10_module.average(lst)
print(f"Average: {avg}")

# Створюємо новий список без повторів
unique_lst = Lab10_module.remove_duplicates(lst)
print(f"List without duplicates: {unique_lst}")
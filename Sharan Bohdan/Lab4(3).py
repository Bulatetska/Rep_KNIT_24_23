# Порахувати за допомогою словника скільки разів елемент повторюється у списку
my_list = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 4, 8, 1]
counts = {}

for item in my_list:
    if item not in counts:
        counts[item] = 1
    else:
        counts[item] += 1

print("Кількість повторів елементів у списку:", counts)
# 1. Виведення елементів A, яких немає в B:
A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}

result = A - B
print(result)

# 2. Виведення спільних елементів А та В:
result = A & B
print(result)

# 3. Виведення об'єднання множин А та В:
result = A | B
print(result)  

# 4. Перевірка, чи всі символи унікальні, використовуючи множини та списки:
a = "a14b6fh"

# перевірка списком
if len(a) == len(set(a)):
    print("Усі символи унікальні за допомогою списку")

# перевірка множиною
if len(a) == len(set(list(a))):
    print("Усі символи унікальні за допомогою множини")

# 5. Підрахунок кількості повторень елементів у списку за допомогою словника:
lst = [1, 2, 3, 2, 1, 1, 4, 2, 5, 4, 2]

result = {}
for item in lst:
    if item not in result:
        result[item] = 1
    else:
        result[item] += 1

print(result)

# 6. Виведення всіх значень словника, які мають парний ключ:
dct = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}

for key, value in dct.items():
    if key % 2 == 0:
        print(value)

# 7. Видалення всіх ключів, значення яких починається з літери "а":
dct = {"apple": 1, "banana": 2, "apricot": 3, "cherry": 4}

keys_to_delete = []
for key, value in dct.items():
    if key.startswith("a"):
        keys_to_delete.append(key)

for key in keys_to_delete:
    del dct[key]

print(dct)

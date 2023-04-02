A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}
print('Завдання 1')
result = [elem for elem in A if elem not in B]
print(result)

print('Завдання 2')
result = [elem for elem in A if elem in B]
print(result)

print('Завдання 3')
result = A.union(B)
print(result)

print('Завдання 4')
a = "a14b6fh"

if len(a) == len(set(a)):
    print("Всі символи унікальні")
else:
    print("Є повторювані символи")

print('Завдання 5')
lst = [1, 2, 3, 2, 1, 1, 4, 5, 4]
result = {}
for elem in lst:
    if elem not in result: 
        result[elem] = 1
    else:
        result[elem] += 1
print(result)

print('Завдання 6')
dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result = [value for key, value in dct.items() if key in 'bdfhjlnprtvxz']
print(result)  

print('Завдання 7')
dct = {'apple': 1, 'banana': 2, 'avocado': 3, 'mango': 4}
keys_to_remove = [key for key in dct.keys() if key.startswith("a")]
for key in keys_to_remove:
    del dct[key]
print(dct)
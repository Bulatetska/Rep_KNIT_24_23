A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}
result1 = A - B
print('1.елементи A, яких немає в B:')
print(result1)
result2 = A & B
print('2.спільні елементи А та В:')
print(result2)
print('3.обєднання множин А та В:')
result3 = A | B
print(result3)

a = "a14b6fh"
unique_chars = set(a)
if len(unique_chars) == len(a):
    print("4. у рядку a14b6fh усі символи унікальні")
else:
    print("4. у рядку a14b6fh не всі символи унікальні")

my_list = [1, 2, 3, 2, 3, 3, 4, 5, 1, 1, 1]
my_dict = {}
for item in my_list:
    if item in my_dict:
        my_dict[item] += 1
    else:
        my_dict[item] = 1
print("5.")
print(my_dict)


my_dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print('6.')
for key in my_dict2.keys():
    if key.isdigit() and int(key) % 2 == 0:
        print(my_dict2[key])

my_dict3 = {'apple': 1, 'banana': 2, 'avocado': 3, 'pear': 4, 'apricot': 5, 'peach': 6}
new_dict = {}
for key, value in my_dict3.items():
    if not key.startswith('a'):
        new_dict[key] = value
print('7.')
print(new_dict)
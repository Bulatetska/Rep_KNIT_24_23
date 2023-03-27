'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print("Завдання 1-3:")
A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}
C = A - B
D = A & B
E = A | B
print("Елемети A, яких немає в B:", C)
print("Спільні елементи А та В:", D)
print("Об'єднання множин А та В:", E)

print("Завдання 4:")
a = "a14b6fh"
unique = set(a)
res1 = len(unique) == len(a)
res2 = all(a.count(char) == 1 for char in a)
print("З використанням множини:", res1)
print("З використанням списку:", res2)

print("Завдання 5:")
a = [1, 1, 2, 2, 3, 4, 5, 1, 5, 2]
counts = {}
for elem in a:
    if elem in counts:
        counts[elem] += 1
    else:
        counts[elem] = 1
print(counts)

print("Завдання 6:")
b = {1: 'music', 2: 'math', 3: 'history', 4: 'biology', 5: 'english'}
for key, value in b.items():
    if key % 2 == 0:
        print(value)
        
print("Завдання 7:")       
c = {1: "banana", 2: "dog", 3: "air", 4: "cat", 5: "analysis"}
keys_to_remove = []

for key, value in c.items():
    if str(value).startswith('a'):
        keys_to_remove.append(key)

for key in keys_to_remove:
    del c[key]

print(c)

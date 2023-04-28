print("Завдання_1\nВведіть довжину списку:")
n = int(input())
print("Введіть список:")
arr = input()
l = list(map(int,arr.split(' ')))
print(l)
for i in l:
    if i%2==0.0:
        l.remove(i)
print(l)
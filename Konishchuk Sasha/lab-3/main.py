print("Завдання_1\nВведіть довжину списку:")
n = int(input())
print("Введіть список:")
arr = input()
l = list(map(int,arr.split(' ')))
print(l)
for i,ind in l:
    print(i,ind)
    if i%2==0.0:
        l.remove(i)
print(l)
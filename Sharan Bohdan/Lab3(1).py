lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lst:
    if i % 2 == 0:
        lst.remove(i)

print(lst)

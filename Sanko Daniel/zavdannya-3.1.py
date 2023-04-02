lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_lst = []
for item in lst:
    if item % 2 != 0:
        new_lst.append(item)
lst = new_lst
print(lst)
elements = [2, -4, 4, 12, 0, 0, -4, 10, 11, -2, -2]
dict = {}

for i in elements:
    dict[i] = dict.get(i, 0) + 1

print (dict)
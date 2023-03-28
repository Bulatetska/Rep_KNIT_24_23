A = (3, 5, 11, 7, 4, -3)
B = (11, 5, 8, 1, 10, 7)

C = []

for i in A:
    if i not in B:
        C += [i]

print("TASK 1: ", C)


C.clear()

for i in A:
    if i in B:
        C += [i]

print("TASK 2: ", C)

# TASK 3
C = list(A + B)

print("TASK 3: ", C)


str1 = "a14b6fr"
list1 = []

result = "unique"

for i in str1:
    if i in list1:
        result = "not unique"
        break
    else:
        list1 += [i]

print("TASK 4: ", result)


array = ["shop", "market", "store", "beard", "market", "beard", "beard", "beard"]

table = {}

for i in array:
    if i in table:
        table[i] += 1
    else:
        table[i] = 1

print("TASK 5: ", table)


dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "yearOld": 1890
}

print("TASK 6:")
i = 1
for key in dict1.keys():
    if i % 2 == 0:
        print(key, ":", dict1[key])
    i += 1



dict2 = {
    "animal": "monkey",
    "model": "Mustang",
    "alpina": 2006,
    "Ukraine": 1991
}

iterObj = iter(dict2)

lst = list(iterObj)

for key in lst:
    if key.startswith("a"):
        del dict2[key]

print("TASK 7:", dict2)
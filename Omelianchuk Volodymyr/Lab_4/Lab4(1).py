A = {3, 5, 11, 7, 4, -3}
B = {11, 5, 8, 1, 10, 7}

print("1) Елементи A, яких немає в B:")
for elem in A:
    if elem not in B:
        print(elem)

print("2) Спільні елементи А та В:")
for elem in A:
    if elem in B:
        print(elem)

print("3) Об'єднання множин А та В:", A.union(B))

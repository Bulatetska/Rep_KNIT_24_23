a = [1, 2, 3, 2, 1, 4, 5, 1, 4, 2]
counts = {}
for elem in a:
    if elem in counts:
        counts[elem] += 1
    else:
        counts[elem] = 1
print(counts)
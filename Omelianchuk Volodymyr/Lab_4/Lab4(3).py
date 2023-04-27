myList = [1, 2, 3, 2, 1, 3, 3, 4, 5, 6, 5, 4, 4]

amount = {}
for elem in myList:
    if elem in amount:
        amount[elem] += 1
    else:
        amount[elem] = 1

print(amount)
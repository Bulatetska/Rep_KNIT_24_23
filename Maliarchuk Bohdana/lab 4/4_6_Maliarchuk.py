dict = {2: 1, -4: 2, 4: 1, 12: 1, 0: 2, 10: 1, 11: 1, -2: 2}

for key in dict.keys():
    if dict.setdefault(key) % 2 == 0:
        print (key)
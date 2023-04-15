list = ["first", "1", 1, 2, "red", "green", "red", "blue"]
slovnuk = {}
for i in list:
    if i in slovnuk:
        slovnuk[i] = slovnuk[i] + 1
    else:
        slovnuk[i] = 1
print(slovnuk)
my_dict = {1: "apple", 2: "book", 3: "cat", 4: "airplane", 5: "house"}
keys_to_remove = []

for key, value in my_dict.items():
    if str(value).startswith('a'):
        keys_to_remove.append(key)

for key in keys_to_remove:
    del my_dict[key]

print(my_dict)
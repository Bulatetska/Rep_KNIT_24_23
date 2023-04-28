# Видалити всі ключі, значення яких починається з літери "а"
my_dict = {"apple": 1, "banana": 2, "orange": 3, "apricot": 4}

keys_to_delete = []

for key, value in my_dict.items():
    if key.startswith("a"):
        keys_to_delete.append(key)

for key in keys_to_delete:
    del my_dict[key]

print(my_dict)
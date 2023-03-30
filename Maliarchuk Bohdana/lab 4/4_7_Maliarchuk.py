dict = {"apple": 1, "book": 2, "a": 1, "show": 1, "snow": 2, "hat": 1, "keys": 1, "any": 2}
dict_copy = dict.copy()

for key in dict.keys():
    if key.startswith('a'):
        dict_copy.pop(key)

print(dict_copy)
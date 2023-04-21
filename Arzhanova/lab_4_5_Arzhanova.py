my_list = {'a': 'A', 'a': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F'}
new_list = []
for key in my_list:
    if key.startswith('a'):
        new_list.append(key)
for key in new_list:
    del my_list[key]
print(my_list)


a = "a14b6fh"

if len(set(a)) == len(a):
    print("Всі символи унікальні")
else:
    print("Є не унікальні символи")

unique_chars = []
for char in a:
    if char not in unique_chars:
        unique_chars.append(char)

if len(unique_chars) == len(a):
    print("Всі символи унікальні")
else:
    print("Є не унікальні символи")

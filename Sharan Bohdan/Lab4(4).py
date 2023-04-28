# Пройтися по словнику і вивести всі значення, які мають парний ключ.
my_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}

for key, value in my_dict.items():
    if key % 2 == 0:
        print(value)
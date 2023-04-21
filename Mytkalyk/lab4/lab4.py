def task1():
    A = {3, 5, 11, 7, 4, -3}
    B = {11, 5, 8, 1, 10, 7}

    result = A.difference(B)
    print(result)


def task2():
    A = {3, 5, 11, 7, 4, -3}
    B = {11, 5, 8, 1, 10, 7}

    result = A.intersection(B)
    print(result)


def task3():
    A = {3, 5, 11, 7, 4, -3}
    B = {11, 5, 8, 1, 10, 7}

    result = A.union(B)
    print(result)


def task4():
    a = "a14b6fh"
    if len(a) == len(set(a)):
        print("Всі символи унікальні.")
    else:
        print("Є повторювані символи.")


def task5():
    my_list = [343, 10, 23, 24, 1, 5, 3, 7, 0, 10, 9]

    count_dictionary = {}
    for i in my_list:
        if i in count_dictionary:
            count_dictionary[i] += 1
        else:
            count_dictionary[i] = 1

    print(count_dictionary)


def task6():
    my_dictionary = {"apple": ["red", "green"], "banana": ["yellow"], "cherry": ["red"], "lemon": ["yellow", "green"], "orange": ["orange"]}

    new_dictionary = {}

    for key, value in my_dictionary.items():
        for color in value:
            if color in new_dictionary:
                new_dictionary[color].append(key)
            else:
                new_dictionary[color] = [key]

    print(new_dictionary)



def task7():
    my_dictionary = {'apple': 'red', 'banana': 'yellow', 'orange': 'orange', 'pear': 'green', 'apricot': 'orange'}

    keys_to_delete = []
    for key, value in my_dictionary.items():
        if value.startswith('a'):
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del my_dictionary[key]

    print(my_dictionary)


print("Задвання 1: ")
task1()
print("Задвання 2: ")
task2()
print("Задвання 3: ")
task3()
print("Задвання 4: ")
task4()
print("Задвання 5: ")
task5()
print("Задвання 6: ")
task6()
print("Задвання 7: ")
task7()

def sort_list(lst):
    try:
        return sorted(lst)
    except TypeError as e:
        print("Помилка сортування:", e)

def find_element(lst, value):
    try:
        if value in lst:
            return lst.index(value)
        else:
            return -1
    except ValueError as e:
        print("Помилка пошуку елемента:", e)

def find_sequence(lst, sequence):
    try:
        indices = []
        seq_len = len(sequence)
        for i in range(len(lst) - seq_len + 1):
            if lst[i:i+seq_len] == sequence:
                indices.append(i)
        return indices
    except TypeError as e:
        print("Помилка пошуку послідовності:", e)

def find_first_min_elements(lst, n=5):
    try:
        return sorted(lst)[:n]
    except TypeError as e:
        print("Помилка пошуку перших мінімальних елементів:", e)

def find_first_max_elements(lst, n=5):
    try:
        return sorted(lst, reverse=True)[:n]
    except TypeError as e:
        print("Помилка пошуку перших максимальних елементів:", e)

def calculate_average(lst):
    try:
        return sum(lst) / len(lst)
    except ZeroDivisionError as e:
        print("Помилка обчислення середнього арифметичного:", e)

def remove_duplicates(lst):
    try:
        return list(set(lst))
    except TypeError as e:
        print("Помилка видалення дублікатів:", e)

def sort_list(lst):
    """
    Сортує список lst за зростанням і повертає його.
    """
    return sorted(lst)

def find_element(lst, val):
    """
    Шукає у списку lst перше входження елементу зі значенням val і повертає його індекс.
    Якщо елемент не знайдено, повертає -1.
    """
    try:
        return lst.index(val)
    except ValueError:
        return -1

def find_sequence(lst, seq):
    """
    Шукає у списку lst перше входження послідовності елементів seq і повертає його індекс.
    Якщо послідовність не знайдено, повертає -1.
    """
    n = len(seq)
    for i in range(len(lst) - n + 1):
        if lst[i:i+n] == seq:
            return i
    return -1

def find_first_n_min(lst, n=5):
    """
    Повертає список перших n мінімальних елементів списку lst.
    """
    return sorted(lst)[:n]

def find_first_n_max(lst, n=5):
    """
    Повертає список перших n максимальних елементів списку lst.
    """
    return sorted(lst, reverse=True)[:n]

def average(lst):
    """
    Обчислює середнє арифметичне значення елементів списку lst і повертає його.
    Якщо список порожній, повертає 0.
    """
    if not lst:
        return 0
    return sum(lst) / len(lst)

def remove_duplicates(lst):
    """
    Повертає список, що сформований з початкового списку lst, але не містить повторів.
    """
    return list(set(lst))

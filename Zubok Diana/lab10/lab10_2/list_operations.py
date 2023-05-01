def sort_list(lst):
    """Сортує заданий список."""
    return sorted(lst)

def find_element(lst, elem):
    """Функція повертає індекс першого знайденого елемента у списку або None, якщо елемент не знайдено."""
    try:
        return lst.index(elem)
    except ValueError:
        return None

def find_sequence(lst, seq):
    """Функція повертає індекс першого елементу з проміжку, якщо проміжок не знайдено повертає None."""
    n = len(seq)
    for i in range(len(lst) - n + 1):
        if lst[i:i + n] == seq:
            return i
    return None

def find_min(lst, n=5):
    """Функція повертає перші 5 мін. елементів"""
    return sorted(lst)[:n]

def find_max(lst, n=5):
    """Функція повертає перші 5 макс. елементів"""
    return sorted(lst, reverse=True)[:n]

def average(lst):
    """Функція провертає середнє арифметичне"""
    return sum(lst) / len(lst)

def remove_duplicates(lst):
    """Функція повертає список, що сформований з початкового списку, але не містить повторів"""
    return list(dict.fromkeys(lst))
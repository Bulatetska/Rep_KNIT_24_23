def sort_list(lst):
    """
    Сортує список у порядку зростання.

    Args:
        lst (list): Список елементів.

    Returns:
        list: Відсортований список.
    """
    return sorted(lst)


def find_element(lst, value):
    """
    Знаходить перший елемент у списку за заданим значенням.

    Args:
        lst (list): Список елементів.
        value: Значення, яке потрібно знайти.

    Returns:
        int: Індекс першого знайденого елемента або -1, якщо елемент не знайдено.
    """
    if value in lst:
        return lst.index(value)
    else:
        return -1


def find_sequence(lst, sequence):
    """
    Знаходить послідовність елементів у списку.

    Args:
        lst (list): Список елементів.
        sequence (list): Послідовність елементів, яку потрібно знайти.

    Returns:
        bool: True, якщо послідовність знайдена, False - у іншому випадку.
    """
    n = len(sequence)
    for i in range(len(lst) - n + 1):
        if lst[i:i + n] == sequence:
            return True
    return False


def find_min_elements(lst, n):
    """
    Знаходить перші n мінімальних елементів у списку.

    Args:
        lst (list): Список елементів.
        n (int): Кількість мінімальних елементів, які потрібно знайти.

    Returns:
        list: Список перших n мінімальних елементів.
    """
    return sorted(lst)[:n]


def find_max_elements(lst, n):
    """
    Знаходить перші n максимальних елементів у списку.

    Args:
        lst (list): Список елементів.
        n (int): Кількість максимальних елементів, які потрібно знайти.

    Returns:
        list: Список перших n максимальних елементів.
    """
    return sorted(lst, reverse=True)[:n]


def calculate_average(lst):
    """
    Обчислює середнє арифметичне значення списку.

    Args:
        lst (list): Список числових значень.

    Returns:
        float: Середнє арифметичне значення.
    """
    return sum(lst) / len(lst)


def remove_duplicates(lst):
    """
    Повертає список, що складається з початкового списку, але без повторів.

    Args:
        lst (list): Список елементів.

    Returns:
        list: Список без повторів.
    """
    return list(dict.fromkeys(lst))

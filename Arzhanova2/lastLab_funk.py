def sort_list(lst):
    """Сортує список за зростанням.

    Args:
        lst (list): Вхідний список.

    Returns:
        list: Відсортований список.
    """
    try:
        return sorted(lst)
    except TypeError:
        raise ValueError("The list contains elements that cannot be sorted.")

def find_element(lst, value):
    """Знаходить перший елемент у списку за заданим значенням.

    Args:
        lst (list): Вхідний список.
        value: Значення, яке шукаємо.

    Returns:
        int: Індекс першого знайденого елемента або -1, якщо елемент не знайдено.
    """
    try:
        return lst.index(value)
    except ValueError:
        return -1

def find_sequence(lst, sequence):
    """Знаходить першу послідовність елементів у списку.

    Args:
        lst (list): Вхідний список.
        sequence (list): Послідовність елементів, яку шукаємо.

    Returns:
        int: Індекс першого елемента знайденої послідовності або -1, якщо послідовність не знайдено.
    """
    n = len(sequence)
    for i in range(len(lst) - n + 1):
        if lst[i:i + n] == sequence:
            return i
    return -1

def find_first_min_elements(lst, n):
    """Знаходить перші n мінімальних елементів у списку.

    Args:
        lst (list): Вхідний список.
        n (int): Кількість мінімальних елементів, які потрібно знайти.

    Returns:
        list: Список перших n мінімальних елементів.
    """
    try:
        sorted_lst = sorted(lst)
        return sorted_lst[:n]
    except TypeError:
        raise ValueError("The list contains elements that cannot be sorted.")

def find_first_max_elements(lst, n):
    """Знаходить перші n максимальних елементів у списку.

    Args:
        lst (list): Вхідний список.
        n (int): Кількість максимальних елементів, які потрібно знайти.

    Returns:
        list: Список перших n максимальних елементів.
    """
    try:
        sorted_lst = sorted(lst, reverse=True)
        return sorted_lst[:n]
    except TypeError:
        raise ValueError("The list contains elements that cannot be sorted.")

def calculate_average(lst):
    """Обчислює середнє арифметичне значення списку.

    Args:
        lst (list): Вхідний список чисел.

    Returns:
        float: Середнє арифметичне значення.
    """
    try:
        if not lst:
            raise ValueError("The list is empty.")
        return sum(lst) / len(lst)
    except TypeError:
        raise ValueError("The list contains elements that cannot be summed.")

def remove_duplicates(lst):
    """Повертає список без повторень (залишається лише перший з однакових елементів).

    Args:
        lst (list): Вхідний список.

    Returns:
        list: Список без повторень.
    """
    try:
        return list(dict.fromkeys(lst))
    except TypeError:
        raise ValueError("The list contains elements that cannot be used as keys.")

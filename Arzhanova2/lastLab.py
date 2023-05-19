def sort_list(lst):
    """Сортує список за зростанням.

    Args:
        lst (list): Вхідний список.

    Returns:
        list: Відсортований список.
    """
    return sorted(lst)


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
    return sorted(lst)[:n]


def find_first_max_elements(lst, n):
    """Знаходить перші n максимальних елементів у списку.

    Args:
        lst (list): Вхідний список.
        n (int): Кількість максимальних елементів, які потрібно знайти.

    Returns:
        list: Список перших n максимальних елементів.
    """
    return sorted(lst, reverse=True)[:n]


def calculate_average(lst):
    """Обчислює середнє арифметичне значення списку.

    Args:
        lst (list): Вхідний список чисел.

    Returns:
        float: Середнє арифметичне значення.
    """
    if not lst:
        return 0
    return sum(lst) / len(lst)


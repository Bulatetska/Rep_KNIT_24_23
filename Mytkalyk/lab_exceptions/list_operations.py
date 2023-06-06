def sort_list(lst):
    """Сортує список за зростанням."""
    return sorted(lst)

def find_element(lst, element):
    """Повертає перше входження елемента в список або None, якщо елемент не знайдено."""
    if element in lst:
        return element
    else:
        return None

def find_sequence(lst, sequence):
    """Повертає True, якщо послідовність елементів знайдена в списку, інакше - False."""
    if len(sequence) > len(lst):
        return False
    for i in range(len(lst) - len(sequence) + 1):
        if lst[i:i+len(sequence)] == sequence:
            return True
    return False

def find_first_min(lst):
    """Повертає список перших п'яти мінімальних елементів."""
    return sorted(lst)[:5]

def find_first_max(lst):
    """Повертає список перших п'яти максимальних елементів."""
    return sorted(lst, reverse=True)[:5]

def calculate_average(lst):
    """Обчислює середнє арифметичне значення елементів списку."""
    if len(lst) == 0:
        return None
    return sum(lst) / len(lst)

def remove_duplicates(lst):
    """Повертає список, що містить унікальні елементи з початкового списку."""
    return list(set(lst))

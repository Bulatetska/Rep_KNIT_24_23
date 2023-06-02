from list_operations import *

def main():
    # Приклад вхідних даних
    numbers = [5, 3, 8, 2, 9, 1, 5, 2, 8]
    print("Дано список:", numbers)

    # Сортування списку
    sorted_numbers = sort_list(numbers)
    print("Відсортований список:", sorted_numbers)

    # Пошук елемента за значенням
    index = find_element(numbers, 9)
    if index != -1:
        print("Елемент 9 шуканий за індексом:", index)
    else:
        print("Елемент не знайдений")

    # Пошук послідовності елементів
    sequence = [2, 9, 1]
    if find_sequence(numbers, sequence):
        print("Послідовність [2, 9, 1] знайдена")
    else:
        print("Послідовність [2, 9, 1] не знайдена")

    # Пошук перших п'яти мінімальних елементів
    min_elements = find_min_elements(numbers, 5)
    print("Перших 5 мінімальних елементів:", min_elements)

    # Пошук перших п'яти максимальних елементів
    max_elements = find_max_elements(numbers, 5)
    print("Перших 5 максимальних елементів:", max_elements)

    # Обчислення середнього арифметичного
    average = calculate_average(numbers)
    print("Середнє значення:", average)

    # Видалення повторів
    unique_numbers = remove_duplicates(numbers)
    print("Список без повторень:", unique_numbers)


if __name__ == "__main__":
    main()

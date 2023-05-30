def sort_and_divide(arr):
    sorted_arr = sorted(arr)  # Сортуємо масив
    min_num = sorted_arr[0]  # Отримуємо найменше число
    result = min_num / 17  # Ділимо найменше число на 17
    print("Sort array:", sorted_arr)
    print("The smallest number:", min_num)
    print("Divide 17:", result)


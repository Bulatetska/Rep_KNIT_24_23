def squareNumbers(arr, result_arr):
    while arr:
        current_number = arr.pop()
        # Імітація друку моделі на 3D-принтері.
        print("Number: " + str(current_number))
        result_arr.append(current_number * current_number)


def printResult(result_arr):
    print("\nThe following squared numbers have been printed:")
    for number in result_arr:
        print(number)


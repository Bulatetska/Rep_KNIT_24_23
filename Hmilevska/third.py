def remove_even_numbers(nums):
    # create a new list with only odd numbers
    return [num for num in nums if num % 2 != 0]

def square_numbers(nums):
    # create a new list with squared numbers
    return [num**2 for num in nums]

def find_max_number(nums):
    # find the max number in the list
    return max(nums)

def main():
    # ask user to enter a list of numbers or use default list
    choice = input("Do you want to enter your own list of numbers? (yes or no): ")
    if choice.lower() == "yes":
        # ask user to input their list of numbers
        nums = [int(num) for num in input("Enter numbers separated by spaces: ").split()]
    else:
        # use default list
        nums = [1, 2, 3, 4, 5]

    # print original list
    print("Original list: ", nums)

    # ask user to choose an option
    print("Options:")
    print("1. Remove even numbers")
    print("2. Square all numbers")
    print("3. Find the maximum number")
    option = int(input("Choose an option (1, 2, or 3): "))

    # perform selected operation on the list and print the result
    if option == 1:
        result = remove_even_numbers(nums)
        print("List with even numbers removed: ", result)
    elif option == 2:
        result = square_numbers(nums)
        print("Squared list: ", result)
    elif option == 3:
        result = find_max_number(nums)
        print("Maximum number: ", result)
    else:
        print("Invalid option")

    # ask user if they want to run the program again
    choice = input("Do you want to run the program again? (yes or no): ")
    if choice.lower() == "yes":
        main()
    else:
        print("Thank you for using the program")

# run the program
main()

def find_max(lst):
    # Find the maximum value in the list
    max_val = max(lst)
    if max_val > 0:
        return max_val
    else:
        return "The number is less than or equal to 0"


def count_letters(word):
    # Count the number of letters in the word
    return len(word)


def power(base, exponent):
    # Raise a number to a positive exponent
    if exponent >= 0:
        return base ** exponent
    else:
        return "Exponent must be non-negative"


def print_numbers(n):
    # Print all numbers from 1 to n
    for i in range(1, n+1):
        print(i)


def rectangle_area(height, width):
    # Calculate the area of a rectangle
    return height * width


def main():
    # Main menu with options for different tasks
    while True:
        print("1. Find the maximum value in a list")
        print("2. Count the number of letters in a word")
        print("3. Raise a number to a positive exponent")
        print("4. Print all numbers from 1 to n")
        print("5. Calculate the area of a rectangle")
        print("6. Quit program")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            lst = input("Enter a list of numbers separated by spaces: ")
            lst = [float(x) for x in lst.split() if x.replace('.', '', 1).isdigit()]
            if lst:
                result = find_max(lst)
                print(result)
            else:
                print("Invalid input. Please enter a list of numbers separated by spaces.")
        elif choice == "2":
            word = input("Enter a word: ")
            result = count_letters(word)
            print(result)
        elif choice == "3":
            base = float(input("Enter a base number: "))
            exponent = int(input("Enter an exponent: "))
            result = power(base, exponent)
            print(result)
        elif choice == "4":
            n = int(input("Enter a number: "))
            print_numbers(n)
        elif choice == "5":
            height = float(input("Enter the height of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            result = rectangle_area(height, width)
            print(result)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice")

        # Ask the user if they want to run the program again
        run_again = input("Do you want to run the program again? (y/n): ")
        if run_again.lower() != "y":
            print("Exiting program...")
            break


if __name__ == "__main__":
    main()

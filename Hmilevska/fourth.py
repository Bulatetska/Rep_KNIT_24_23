def unique_chars(string):
    # Check if all characters are unique using sets
    unique_chars = set(string)
    if len(unique_chars) == len(string):
        print("All characters are unique")
    else:
        print("There are repeating characters")

    # Check if all characters are unique using lists
    char_list = []
    for char in string:
        if char in char_list:
            print("There are repeating characters")
            break
        char_list.append(char)
    else:
        print("All characters are unique")


def count_elements(lst):
    # Count how many times each element appears in a list
    counts = {}
    for elem in lst:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1

    print(counts)


def even_key_values(my_dict):
    # Print values in dictionary with even keys
    for key, value in my_dict.items():
        if key % 2 == 0:
            print(value)


def remove_a_keys(my_dict):
    # Remove keys from dictionary that start with 'a'
    for key in list(my_dict.keys()):
        if key.startswith("a"):
            del my_dict[key]

    print(my_dict)


def main():
    # Initialize data for the program
    A = {3, 5, 11, 7, 4, -3}
    B = {11, 5, 8, 1, 10, 7}
    a = "a14b6fh"
    my_list = [3, 5, 11, 7, 4, 3, 11, 5, 7, 3, 11]
    my_dict = {"apple": 3, "banana": 5, "cherry": 11, "date": 7, "elderberry": 4}

    # Main menu with options for different tasks
    while True:
        print("1. Print elements in A that are not in B")
        print("2. Print common elements in A and B")
        print("3. Print union of A and B")
        print("4. Check if all characters in a string are unique")
        print("5. Count how many times each element appears in a list")
        print("6. Print values in dictionary with even keys")
        print("7. Remove keys from dictionary that start with 'a'")
        print("8. Quit program")
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            result = A - B
            print(result)
        elif choice == "2":
            result = A & B
            print(result)
        elif choice == "3":
            result = A | B
            print(result)
        elif choice == "4":
            unique_chars(a)
        elif choice == "5":
            count_elements(my_list)
        elif choice == "6":
            even_key_values(my_dict)
        elif choice == "7":
            remove_a_keys(my_dict)
        elif choice == "8":
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

# Task 1: Calculate discounted price
def calculate_discounted_price():
    price = float(input("Enter the price of the product: "))
    discount = 0

    if price > 1000:
        discount = 0.1
    elif price > 500:
        discount = 0.05
    elif price > 100:
        discount = 0.03

    if discount > 0:
        final_price = price - (price * discount)
        print("Price with discount: ", final_price)
    else:
        print("No discount available for this product, price remains the same - ", price)


# Task 2: Check for empty string using ternary operator
def check_empty_string(str):
    return str if str != "" else None


# Main function
def main():
    task_choice = int(input("Choose task (1 or 2): "))

    if task_choice == 1:
        calculate_discounted_price()
    elif task_choice == 2:
        input_string = input("Enter a string: ")
        result = check_empty_string(input_string)
        print("Result: ", result)
    else:
        print("Invalid task choice")

    # Ask user if they want to run the program again or exit
    choice = input("Do you want to run the program again? (yes or no): ")
    if choice.lower() == "yes":
        main()
    elif choice.lower() == "no":
        print("Thank you for using the program")
    else:
        print("Invalid choice")

# run the program
main()
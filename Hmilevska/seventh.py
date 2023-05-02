import string
import random
import datetime
import json

def generate_random_string():
    # Define the alphabet
    alphabet = string.ascii_lowercase
    # Generate a random string of 25 characters using the alphabet
    random_string = ''.join(random.choice(alphabet) for i in range(25))
    # Write the random string to a file named random_string.txt
    with open('random_string.txt', 'w') as f:
        f.write(random_string)

def generate_user_data():
    # Define a list of users
    users = ["Artur", "Kate", "Alisa", "Mike"]
    user_data = []
    # Loop through the list of users and generate a dictionary for each user with a random age
    for user in users:
        user_age = random.randint(1, 99)
        user_dict = {"name": user, "age": user_age}
        user_data.append(user_dict)
    # Create a dictionary containing the list of user dictionaries and the current date/time
    created_at = datetime.datetime.now().strftime("%d;%m;%y")
    data = {"data": user_data, "created_at": created_at}
    # Write the dictionary to a JSON file named users_data_{current_date}.json
    with open(f"users_data_{created_at}.json", "w") as file:
        json.dump(data, file, indent=4)

def main():
    # Display menu options to the user
    while True:
        print("1. Generate random string and save it to file")
        print("2. Generate user data and save it to JSON file")
        print("3. Quit program")
        # Ask the user to choose an option
        choice = input("Enter your choice (1-3): ")
        # Execute the chosen option
        if choice == "1":
            generate_random_string()
            print("Random string generated and saved to file.")
        elif choice == "2":
            generate_user_data()
            print("User data generated and saved to file.")
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice")
        # Ask the user if they want to run the program again
        run_again = input("Do you want to run the program again? (y/n): ")
        # If the user doesn't want to run the program again, exit the loop
        if run_again.lower() != "y":
            print("Exiting program...")
            break

if __name__ == "__main__":
    main()

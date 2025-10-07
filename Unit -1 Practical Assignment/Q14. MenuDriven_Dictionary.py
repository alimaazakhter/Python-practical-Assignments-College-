# Menu driven dictionary program

# Step 1: Dictionary input from user
n = int(input("Enter number of items in dictionary: "))
my_dict = {}

for i in range(n):
    key = input(f"Enter key: ")
    value = input(f"Enter value for: ")
    my_dict[key] = value

print("\nOriginal Dictionary:", my_dict)

# Step 2: Menu
while True:
    print("\nMenu:")
    print("1. Check if a key exists")
    print("2. Remove a key")
    print("3. Sort dictionary by key")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        check_key = input("Enter key to check: ")
        if check_key in my_dict:
            print("Key exists in dictionary")
        else:
            print("Key does not exist")

    elif choice == 2:
        remove_key = input("Enter key to remove: ")
        removed_value = my_dict.pop(remove_key, None)

        if removed_value is None:
            print(f"Key '{removed_value}' not found in the dictionary.")
        else:
            print(f"Key '{removed_value}' removed successfully. Removed value: {removed_value}")
        print('After removing key: ', my_dict)        

    elif choice == 3:
        sorted_dict = dict(sorted(my_dict.items()))
        print("Dictionary sorted by key:", sorted_dict)

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice, please try again")

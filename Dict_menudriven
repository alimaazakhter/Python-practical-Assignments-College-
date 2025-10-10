my_dict = {}
n = input("Enter number of elements here: ")
if n == "":       # agar user blank enter kare
    print("No input given. Exiting program...")
    exit()
    
elif not n.isdigit():
    print("Invalid input. Exiting program...")
    exit()    
else:
    n = int(n)    

for i in range(n):
    key = input("Enter key here: ")
    value = input("Enter value here: ")
    my_dict[key] = value

while True:
    print("\n*******Dictionary Menu*******")
    print("1. Check if a key exists.")
    print("2. Remove a key")
    print("3. Sort dictionary by key")
    print("4. Exit")

    choice = input("Enter your choice between (1-4): ")
    if choice == "" or not choice.isdigit():
        choice = 0
    else:
        choice = int(choice)

    if choice == 1:
        check_key = input("Enter key to check: ")
        if check_key in my_dict:
            print("The key exists. Value =", my_dict[check_key])
        else:
            print("The key doesn't exist.")

    elif choice == 2:
        remove_key = input("Enter any key to remove: ")
        if remove_key in my_dict:
            removed_value = my_dict.pop(remove_key)
            print(f"Key '{remove_key}' removed. Value was '{removed_value}'")
        else:
            print(f"Key '{remove_key}' not found in dictionary.")

    elif choice == 3:
        if my_dict == {}:
            print("Dictionary is empty. Nothing to sort.")
        else:
            sorted_dict = dict(sorted(my_dict.items()))
            print("Your sorted dictionary:", sorted_dict)

    elif choice == 4:
        print("Exit program")
        break

    else:
        print("Invalid Input. Please enter between 1-4.")

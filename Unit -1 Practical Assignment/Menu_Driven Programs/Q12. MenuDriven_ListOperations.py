# Menu Driven List Operations

# Input list from user
lst = []
n = int(input("Enter number of elements in list: "))
for i in range(n):
    element = int(input("Enter element: "))
    lst.append(element)

while True:
    print("\n===== LIST OPERATIONS MENU =====")
    print("1. Remove duplicates from list")
    print("2. Get largest and smallest number")
    print("3. Check if list is empty or not")
    print("4. Multiply all items in list")
    print("5. Retrieve only negative numbers")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        new_list = []
        for i in lst:
            if i not in new_list:
                new_list.append(i)
        print("List after removing duplicates:", new_list)

    elif choice == 2:
        if len(lst) == 0:
            print("List is empty!")
        else:
            largest = max(lst)   # using max()
            smallest = min(lst)  # using min()
            print("Largest:", largest)
            print("Smallest:", smallest)

    elif choice == 3:
        if len(lst) == 0:
            print("The list is empty")
        else:
            print("The list is NOT empty:", lst)

    elif choice == 4:
        result = 1
        for i in lst:
            result *= i
        print("Multiplication of all items:", result)

    elif choice == 5:
        negatives = []
        for i in lst:
            if i < 0:
                negatives.append(i)
        if len(negatives) == 0:   # check if no negatives found
            print("No negative numbers in the list")
        else:
            print("Negative numbers in list:", negatives)


    elif choice == 6:
        print("Exiting... Bye!")
        break

    else:
        print("Invalid choice! Try again.")

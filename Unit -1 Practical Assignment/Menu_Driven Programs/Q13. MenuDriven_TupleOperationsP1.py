# ===== MENU DRIVEN TUPLE OPERATIONS (Predefined Tuples) =====

# Already defined tuples
t1 = (5, 2, 9, 5)
print(t1)
t2 = (11, 22, 33)
print(t2)
t3 = (7, 7, 7, 7, 7)
print(t3)


while True:
    print("\n===== TUPLE OPERATIONS MENU =====")
    print("1. Reverse the Tuple")
    print("2. Swap two tuples")
    print("3. Calculate Sum of tuple elements")
    print("4. Check if all elements of tuple are same")
    print("5. Sort the tuple in descending order")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # a) Reverse tuple
    if choice == 1:
        rev = t1[::-1]
        print("Original tuple:", t1)
        print("Reversed tuple:", rev)

    # b) Swap tuples
    elif choice == 2:
        print("Before swapping:")
        print("Tuple 1:", t1)
        print("Tuple 2:", t2)
        t1, t2 = t2, t1   # swapping
        print("After swapping:")
        print("Tuple 1:", t1)
        print("Tuple 2:", t2)

    # c) Sum of tuple elements
    elif choice == 3:
        total = sum(t1)
        print("Tuple:", t1)
        print("Sum of elements:", total)

    # d) Check if all elements same
    elif choice == 4:
        if t3.count(t3[0]) == len(t3):
         print("All the elements are same")
        else:
         print("Elements are different")

    # e) Sort tuple in descending order
    elif choice == 5:
        sorted_tuple = tuple(sorted(t1, reverse=True))
        print("Original tuple:", t1)
        print("Tuple sorted in descending order:", sorted_tuple)

    # Exit
    elif choice == 6:
        print("Exiting... Bye!")
        break

    else:
        print("Invalid choice! Try again.")

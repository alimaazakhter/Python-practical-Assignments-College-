# ===== MENU DRIVEN TUPLE OPERATIONS =====

# Step 1: Input first tuple
n = int(input("Enter number of elements in first tuple: "))
t1 = []
for i in range(n):
    element = int(input(f"Enter element: "))
    t1.append(element)
t1 = tuple(t1)

# Step 2: Input second tuple (for swapping option)
m = int(input("Enter number of elements in second tuple: "))
t2 = []
for i in range(m):
    element = int(input(f"Enter element: "))
    t2.append(element)
t2 = tuple(t2)

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
        rev2 = t2[::-1]
        print("Original tuple:", t1)
        print("Reversed tuple:", rev)
        print("Original tuple:", t2)
        print("Reversed tuple:", rev2)

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

        sum1 = sum(t1)
        sum2 = sum(t2)
        print("Tuple:", t1)
        print("Sum of elements:", sum1)
        print("Tuple:", t2)
        print("Sum of elements:", sum2)

    # d) Check if all elements same
    elif choice == 4:

        number = t1   # you can change to tuple1 also
        if number.count(number[0]) == len(number):
            print("All the elements are same")
        else:
            print("Elements are different")

        number = t2   # you can change to tuple1 also
        if number.count(number[0]) == len(number):
            print("All the elements are same")
        else:
            print("Elements are different")

    # e) Sort tuple in descending order
    elif choice == 5:

        sorted_tuple1 = tuple(sorted(t1, reverse=True))
        sorted_tuple2 = tuple(sorted(t2, reverse=True))
        print("Original tuple:", t1)
        print("Tuple sorted in descending order:", sorted_tuple1)
        print("Original tuple:", t2)
        print("Tuple sorted in descending order:", sorted_tuple2)

    # Exit
    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")

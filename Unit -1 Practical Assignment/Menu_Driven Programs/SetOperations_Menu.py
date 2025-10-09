# Menu driven program for Set Operations (Safe Input Version)

# Step 1: Input sets from user
n1 = input("Enter number of elements in Set A: ")
if n1 == "" or not n1.isdigit():
    print("No valid input for Set A. Exiting program...")
    exit()
else:
    n1 = int(n1)

setA = set()
for i in range(n1):
    element = input(f"Enter element for Set A: ")
    setA.add(element)

n2 = input("Enter number of elements in Set B: ")
if n2 == "" or not n2.isdigit():
    print("No valid input for Set B. Exiting program...")
    exit()
else:
    n2 = int(n2)

setB = set()
for i in range(n2):
    element = input(f"Enter element for Set B: ")
    setB.add(element)

print("\nSet A:", setA)
print("Set B:", setB)

# Step 2: Menu
while True:
    print("\n===== SET OPERATIONS MENU =====")
    print("1. Union of two sets")
    print("2. Intersection of two sets")
    print("3. Difference of two sets (A - B)")
    print("4. Symmetric Difference")
    print("5. Check if A is subset of B")
    print("6. Check if A is superset of B")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")
    if choice == "" or not choice.isdigit():
        choice = 0  # invalid choice
    else:
        choice = int(choice)

    if choice == 1:
        print("Union:", setA | setB)

    elif choice == 2:
        print("Intersection:", setA & setB)

    elif choice == 3:
        print("Difference (A - B):", setA - setB)

    elif choice == 4:
        print("Symmetric Difference:", setA ^ setB)

    elif choice == 5:
        print("Is A subset of B?:", setA.issubset(setB))

    elif choice == 6:
        print("Is A superset of B?:", setA.issuperset(setB))

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again!")

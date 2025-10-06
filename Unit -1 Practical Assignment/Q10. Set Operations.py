# Python program to perform various set operations manually

# Step 1: User inputs for Set A
set_a = set(map(int, input("Enter elements of Set A separated by space: ").split()))

# Step 2: User inputs for Set B
set_b = set(map(int, input("Enter elements of Set B separated by space: ").split()))

# Display menu
print("\nChoose operation you want to perform:")
print("1. Union")
print("2. Intersection")
print("3. Difference (A - B)")
print("4. Symmetric Difference")
print("5. Check if A is Subset of B")
print("6. Check if A is SuperSet of B")

# User selects operation
choice = int(input("Enter your choice (1-6): "))

# Perform operation based on choice
if choice == 1:
    print("Union of A and B:", set_a | set_b)  # or set_a.union(set_b)
elif choice == 2:
    print("Intersection of A and B:", set_a & set_b)  # or set_a.intersection(set_b)
elif choice == 3:
    print("Difference (A - B):", set_a - set_b)  # or set_a.difference(set_b)
elif choice == 4:
    print("Symmetric Difference:", set_a ^ set_b)  # or set_a.symmetric_difference(set_b)
elif choice == 5:
    if set_a.issubset(set_b):
        print("A is a subset of B")
    else:
        print("A is NOT a subset of B")
elif choice == 6:
    if set_a.issuperset(set_b):
        print("A is a superset of B")
    else:
        print("A is NOT a superset of B")
else:
    print("Invalid choice! Please select 1-6.")

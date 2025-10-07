# Menu Driven String Operations (Simple Version)

s = input("Enter initial string: ")

while True:
    print("\n===== STRING OPERATIONS MENU =====")
    print("1. Count number of vowels")
    print("2. Count length of string (without len())")
    print("3. Reverse string")
    print("4. Find and Replace substring")
    print("5. Check Palindrome")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        vowels = "aeiouAEIOU"
        count = 0
        for ch in s:
            if ch in vowels:
                count += 1
        print("Number of vowels:", count)

    elif choice == 2:
        count = 0
        for ch in s:
            count += 1
        print("Length of string:", count)

    elif choice == 3:
        rev = ""
        for ch in s:
            rev = ch + rev
        print("Reversed string:", rev)

    elif choice == 4:
        old = input("Enter substring to find: ")
        new = input("Enter new substring: ")
        s = s.replace(old, new)
        print("String after replacement:", s)

    elif choice == 5:
        rev = s[::-1]
        if s == rev:
            print("The string is a Palindrome")
        else:
            print("The string is NOT a Palindrome")

    elif choice == 6:
        print("Exiting... Bye!")
        break

    else:
        print("Invalid choice! Try again.")

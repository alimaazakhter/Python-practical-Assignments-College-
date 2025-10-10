# Menu Driven String Operations (Simple Version)

s = input("Enter initial string: ")
if s == "":
    print("Invalid. Exit")
    exit()
else:
    s=str(s)
        
while True:
    print("\n===== STRING OPERATIONS MENU =====")
    print("1. Count number of vowels")
    print("2. Count length of string (without len())")
    print("3. Reverse string")
    print("4. Find and Replace substring")
    print("5. Check Palindrome")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "" or not choice.isdigit():
        print("Choice is empty. Try again")
        continue
    else:
        choice=int(choice)


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
        rev = ""                                                    #rev = s[::-1]
        for ch in s:                                                #print("Reversed string:", rev)
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

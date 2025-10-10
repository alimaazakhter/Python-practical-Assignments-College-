n = input("Enter number of elements in list: ")
lst = []
if n == "" or not n.isdigit():
    print("Invalid. Exit")
    exit()
else:
    n=int(n)

for i in range(n):
    elements=int(input("Enter any element"))
    if elements == "":
        print("The list is empty")
        exit()
    else:     
        lst.append(elements)

print("List: ", lst)

while True:
    print("\n===== LIST OPERATIONS MENU =====")
    print("1. Remove duplicates from list")
    print("2. Get largest and smallest number")
    print("3. Check if list is empty or not")
    print("4. Multiply all items in list")
    print("5. Retrieve only negative numbers")
    print("6. Exit")

    choice = input("enter any choice: ")
    if choice == "" or not choice.isdigit():
        print("Invalid", exit)
        exit()
    else:
        choice=int(choice)

    if choice == 1:
        new_list=[]
        for i in lst:
            if i not in new_list:
                new_list.append(i)
        if len(new_list) == len(lst):
            print("No duplicates in list")
        else:
            print("List after removing duplicates:", new_list)

    elif choice == 2:
        if lst == "":
            print("List is empty", lst)
        else:     
            largest = max(lst)
            Smallest = min(lst)
            print("Largest", largest)
            print("Smallest", Smallest)
    elif choice == 3:
        if len(lst) == 0:
             print("The list is empty")
        else:
            print("The list is NOT empty:", lst)

    elif choice == 4:
         result= 1
         for i in lst:
             result *= i
         print("Multiplication of all items:", result)

    elif choice == 5:
        negative_lst = []
        for i in lst:
            if i < 0:
                negative.append(i)
                
        if len(negatives) == 0:   # check if no negatives found
            print("No negative numbers in the list")
        else:
            print("Negative numbers in list:", negatives)


    elif choice == 6:
        print("Exiting... Bye!")
        break
            
   
                
        







    

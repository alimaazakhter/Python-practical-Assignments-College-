# 6. Write a Python program to perform following operation on given list:      
   
# a)remove duplicates from a list.

# num1 = [5, 2, 8, 2, 3, -1, 8, 6, -1]

# # Create an empty list to store unique elements
# Final_number = []

# # Loop through each number in the original list
# for num in num1:
#     # If the number is not already in unique_numbers, add it
#     if num not in Final_number:
#         Final_number.append(num)

# # Print the list after removing duplicates
# print("Final List after removing duplicates:", Final_number)

#---------------------------------------------------------------------------------------------------------------

# b)get the largest and smallest number from a list.

# num = [5, 2, 8, 2, 3, -1, 8, 6, -1]

# # Get the largest number
# largest = max(num)

# # Get the smallest number
# smallest = min(num)

# # Print results
# print("Largest number in the list:", largest)
# print("Smallest number in the list:", smallest)

#---------------------------------------------------------------------------------------------------------------

# c) Find the list is empty or not

# num = []

# if len(num) == 0:
#     print("The list is Empty")
# else:
#     print("The list is not empty")    

#---------------------------------------------------------------------------------------------------------------

# d) multiply all the items in a list.

# numbers = [1, 2, 2, 3]

# #Step 1: Start with result = 1
# total = 1

# #Step 2: Loop through each number in the list
# for num in numbers:
#     total *= num  # multiply current number with result

# # Step 3: Print the final result
# print("Multiplication of all items:", total)

#---------------------------------------------------------------------------------------------------------------

# e) retrieve only negative numbers from list of numbers.

numbers = [4, -2, 8, -5, 8, 7, -1]

# Create an empty list to store negative numbers
negative_no = []

# Loop through each number in the list
for num in numbers:
    if num < 0:           # check if number is negative
        negative_no.append(num)  # add negative number to list

# Print the negative numbers
print("Negative numbers are :", negative_no)

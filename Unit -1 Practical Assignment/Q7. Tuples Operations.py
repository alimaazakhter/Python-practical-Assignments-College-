# Q7. Write a Python program to perform following operation on given tuple:
    
# a) Reverse the Tuple

# numbers = (10, 20, 30, 40, 50)

# # Reverse using slicing
# reversed_tuple = numbers[::-1]

# print("Original Tuple:", numbers)
# print("Reversed Tuple:", reversed_tuple)

#---------------------------------------------------------------------------------------------------------------

# b) Swap the Tuple

# Method 1 

# Two tuples
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

print("Before Swapping:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# Swapping
tuple1, tuple2 = tuple2, tuple1

print("\nAfter Swapping:")
print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)

# Method 2

# Using Temporary Variable 

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)

# temp = tuple1
# tuple1 = tuple2
# tuple2 = temp

#---------------------------------------------------------------------------------------------------------------

# c) Calculate Sum of tuple elements

# Built-in sum()

# numbers = (10, 20, 30, 40)
# total = sum(numbers)
# print("Sum of tuple elements:", total)

#Method 2: For Loop se
# numbers = (10, 20, 30, 40)
# total = 0

# for num in numbers:
#     total += num

# print("Sum of tuple elements:", total)

#---------------------------------------------------------------------------------------------------------------

# d) Check if all the elements in tuples are same

# number = (7,7,7,7,7)

# if number.count(number[0]) == len(number):
#     print("All the elements are same")
# else :
#     print("Elements are different") 
 
#---------------------------------------------------------------------------------------------------------------

# e) Sort numbers in descending order

# Method 1: Using sorted() function

numbers= (10, 70, 30, 80, 40, 20, 60, 50)

sort_num = tuple(sorted(numbers, reverse=True))

print("Numbers in Descending Order are : ", sort_num)
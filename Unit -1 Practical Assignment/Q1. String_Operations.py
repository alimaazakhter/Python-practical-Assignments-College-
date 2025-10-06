#String Operations Program

# 1. Write a Python program to perform following operation on given string
# input:
#         a) Count Number of Vowel in given string 
#         b) Count Length of string (do not use Len ())
#         c) Reverse string
#         d) Find and replace operation
#         e) check whether string entered is a palindrome or not   



# a) Count Number of Vowel in given string 
# text = input("Enter a string: ")

# vowels = "aeiouAEIOU"           # Count number of vowels
# count = 0
# for ch in text:
#     if ch in vowels:
#         count += 1
# print("Number of vowels:", count) 

#---------------------------------------------------------------------------------------------------------------

# b) Count length of string without using len()
# text = input("Enter a string: ")
# length = 0
# for ch in text:
#     length += 1
# print("Length of string:", length)

# Code with len()

# text = input("Enter a string: ")
# length = len(text)
# print("Length of string:", length)

#---------------------------------------------------------------------------------------------------------------

# c) Reverse string
# text = input("Enter a string: ")
# rev = ""
# for ch in text:
#     rev = ch + rev
# print("Reversed string:", rev)

#---------------------------------------------------------------------------------------------------------------

# d) Find and replace
# text = input("Enter a string: ")
# find_word = input("Enter word/char to find: ")
# replace_word = input("Enter word/char to replace with: ")
# new_string = text.replace(find_word, replace_word)
# print("After replace:", new_string)

#---------------------------------------------------------------------------------------------------------------

# e) Palindrome check

text = input("Enter a string: ")
rev = ""

# reverse string banaye
for char in text:
    rev = char + rev

# palindrome check
if text == rev:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

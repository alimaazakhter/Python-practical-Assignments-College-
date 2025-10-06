# Simple program to check vowel or consonant

# User se input lo
# char = input("Enter a single alphabet: ")

# # Lowercase me convert karo taaki A ya a dono handle ho jaye
# char = char.lower()

# # Check agar input valid alphabet hai
# if len(char) == 1 and char.isalpha():
#     if char in "aeiou":
#         print(char, "is a vowel")
#     else:
#         print(char, "is a consonant")
# else:
#     print("Please enter only one alphabet")

ch = input("Enter the Alphabet: ")

if ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print(ch, "is a vowel")

else:
    print(ch, "is a consonant")


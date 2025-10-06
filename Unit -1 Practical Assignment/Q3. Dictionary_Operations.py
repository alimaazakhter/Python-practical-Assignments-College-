# 3.  Write a Python program to perform following operations on given dictionary input:     
#        a) check whether a given key already exists in a dictionary.
#        b) remove a key from a dictionary. 
#        c) sort a given dictionary by key.

#---------------------------------------------------------------------------------------------------------------

# a) check whether a given key already exists in a dictionary.

#Using in keyword
# dept = {'bca' : 780, 'bba': 500, 'mba': 650, 'mca': 200}
# check_key = input("Enter any key to check: ")

# if check_key in dept:
#     print(f"Yes, this key '{check_key}' exists.")
# else:
#     print(f"No, this key '{check_key}' does not exist.")

# #Using get() method
# dept = {'bca' : 780, 'bba': 500, 'mba': 650, 'mca': 200}
# key_to_check = input("Enter a key to check: ")

# if dept.get(check_key) is not None:
#     print(f"Yes, the key '{check_key}' exists.")
# else:
#     print(f"No, the key '{check_key}' does not exist.")

#Using keys() method
# dept = {'bca' : 780, 'bba': 500, 'mba': 650, 'mca': 200}
# check_key = input("Enter a key to check: ")

# if check_key in dept.keys():
#     print(f"Yes, the key '{check_key}' exists.")
# else:
#     print(f"No, the key '{check_key}' does not exist.")

#---------------------------------------------------------------------------------------------------------------

# b) remove a key from a dictionary.

my_dict = {'CS': 'Computer Science', 'IT': 'Information Technology', 'EE': 'Electrical Engineering'}
key_to_remove = input("Enter the key you want to remove: ")

# Remove key using pop()
removed_value = my_dict.pop(key_to_remove, None)

if removed_value is None:
    print(f"Key '{key_to_remove}' not found in the dictionary.")
else:
    print(f"Key '{key_to_remove}' removed successfully. Removed value: {removed_value}")

# Print updated dictionary
print(my_dict)

#---------------------------------------------------------------------------------------------------------------

# Example dictionary
# c) sort a given dictionary by key
# dict1 = {'b': 'bear', 'a': 'Alien', 'c': 'Cat', 'e': 'elephant', 'd': 'donkey'}

# # Sorting dictionary by key
# sorted = dict(sorted(dict1.items()))

# print("Dictionary sorted by key:", sorted)



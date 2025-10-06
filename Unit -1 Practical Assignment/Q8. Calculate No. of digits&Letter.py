# Take input from user
text = input("Enter any string: ")

# Initialize counters
letter_count = 0
digit_count = 0

# Loop through each character
for ch in text:
    if ch.isalpha():   # check if character is a letter
        letter_count += 1
    elif ch.isdigit(): # check if character is a digit
        digit_count += 1

# Display results
print("Number of letters:", letter_count)
print("Number of digits:", digit_count)

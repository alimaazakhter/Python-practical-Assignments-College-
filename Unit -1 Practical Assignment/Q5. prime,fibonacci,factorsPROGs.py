# Q1. Prime Number

# Take input from user
# n = int(input("Enter a number: "))

# print("Prime numbers up to", n, "are:")

# # Loop through all numbers from 2 to n
# for num in range(2, n + 1):
#     is_prime = True  # assume num is prime
    
#     # Check if num is divisible by any number from 2 to num-1
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False  # num is not prime
#             break  # no need to check further
    
#     # If num is prime, print it
#     if is_prime:
#         print(num, end=" ")

# num = int(input("Enter any number: "))

# if num <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
  
#---------------------------------------------------------------------------------------------------------------

# Q2. Fibonacci Series

# n = int(input("Enter any number: "))
# a = 0
# b = 1

# print("Fibonacci series:")
# for i in range(n):
#     print(a, end=" ")   # har step pe current number print karo
#     fact = a + b
#     a = b
#     b = fact

#---------------------------------------------------------------------------------------------------------------

# Q3. Display Factors of the given number

n = int(input("Enter any number: "))
print(f"\nFactors of {n}:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()
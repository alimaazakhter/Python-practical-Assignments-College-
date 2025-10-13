'''
#Function Global
def icard():
    pass

#method() local
class student:
    def admission(args):
        pass
    def marksheet(args):
        pass

class faculty:
    def subject():
        pass
    def Attendance():
        pass

#class : Is the blueprint of object. It has all the information about object.
'''
'''
#lambda function
def add(no1,no2):
    sum=no1+no2
    return sum

ans = add(10,20)
print("Addition: ", ans(10,20))

#Syntax of lambda
no1=10
no2=20
ans=lambda no1, no2 : no1+no2
print("Addition: :", ans(10,20))
'''
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
addition=lambda num1, num2 : num1+num2
print("Addition: ", addition(num1, num2))

square=lambda num1: num1*num1
print("Square: ", square(num1))

cube= lambda num2: num2*num2*num2
print("Cube: ", cube(num2))

product= lambda num1, num2: num1*num2
print("Product: ", product(num1,num2))

swap= lambda num1,num2: (num2,num1)
print("Before swapping: ", num1, num2)
print("After swapping: ", swap(num1, num2))

#syntax of filter

list1=[]
n = int(input("Till how many numbers: "))
for n in range(1, n+1):
    list1.append(n)
print(list1)

even = filter(lambda n:n%2==0, list1)
print("Even no: ", list(even))

even = tuple(filter(lambda n:n%2==0, list1))
print("Even no: ", even)
#product = lambda num1, num2: num1

#list using range

str1 = "Hello"
vowels= list(filter(lambda char=char in 'aeiouAEIOU', str1))
print(f"Vowel in {str1} are {vowels}")




    



# if-else

# syntax 
"""
if condition:
    # code to execute if condition is true
    pass
else:
    # code to execute if condition is false
    pass
    """

    #  if - else statement
#  find the value whether it is positive negative or zero
n = int(input("Enter a number:" ))
if n>0:
    print(n, "is Positive")
elif n<0:
    print(n, "is Negative")
else:
    print(n, "is Null")


# find the no. whether it is  Even or ODD
n = int(input("Enter a number : "))
if n%2 == 0:
    print(n , "is Even")
else:
    print(n, " is ODD")


# Greater between two numbers
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
if a>b:
    print(a," is Greater than", b)
    print("a is Greater")
elif a==b:
    print(a,"is Equal to",b)
    print("Both are equal")
else:
    print(b,"is Greater than", a)
    print("b is Greater")


# check whether number is Equal or Not Equal 
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
if a == b:
    print("Both are equal")
else:
    print("Both are not equal")


# Voting elgibility
age = int(input("Enter your age : "))
if age >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")



# Divisible by 5 or not 
num = int(input("Enter the number :"))
if (num % 5 == 0):
    print(num , "is divisible by 5")
else:
    print(num , "is not divisible by 5")


# Divisible by 3 and 5
num = int(input("Enter the number : "))
if (num % 3 == 0) and (num % 5 == 0):
    print(num , "is divisible by 3 and 5")
else:
    print(num , "is not divisible by 3 and 5")


# FIND LARGEST FROM THREE NUMBERS 
a= int(input("Enter first value :"))
b= int(input("enter second value :"))
c= int(input("Enter third value :"))
if (a>b) and (a>c):
    print("a is greter than b & c")
elif (b>a) and (b>c):
    print("b is greater than a & c")
else:
    print("c is greater than a & b") 


# Student Grade Calculator
marks = int(input("Enter your marks :"))
if marks>100 or marks <0:
    print ("Invalid marks")
elif marks>=90:
    print("You got A Grade")
elif 90<marks>=80:
    print("You got B grade")
elif 80<marks>=70:
    print("You got C grade")
elif 70<marks>=60:
    print("You got D grade")
else:
    print("Sorry , You are Failed")


# Temperature Classification
temp = float(input("enter the temperature :"))
if temp>40:
    print("It is a Hot day")
elif 40>=temp>20:
    print("It's a shiny day")
elif 20>=temp>0:
    print("It is a cold day")
else:
    print("It's a freezing day")

# 11. Number Classification
          # Positive even
          # Positive odd
          # Negative even
          # Negative odd
          # Zero
num = int(input("Enter a number: "))
if (num>0) and (num% 2 == 0):
    print(num,"is Positive even")
elif (num>0) and (num% 2 == 1):
    print(num,"is Positive odd")
elif (num<0) and (num%2 == 0):
    print(num,"is Negative even")
elif (num<0) and (num % 2 == 1):
    print(num,"is Negative odd")
else:
    print(num,"is Zero")


# Simple Calculator
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))

print("Addition : ", num1 + num2)
print("Subtraction : ", num1 - num2)
print("Multiplication", num1 * num2)
print("Division", num1 / num2)


#  Leap year
year = int(input("enter the year :"))
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")



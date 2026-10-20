# python is an interpreted language
# python is a high level language

# print statement
print("Hello Himanshu");

# variable
a = 5
print(a)

# print a value after using operator
a = 5
b = 10
c= a+b
print(c)

# input value
a = int(input("Enter the value of a = "))
b= int(input("Enter the value of b = "))
print("Total sum = ", a+b)


#  take 3 numbers and product them
a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))
c = int(input("Enter the value of c = "))
sum = a+b+c
print ("total product = ",sum)

# take 2 numbers and average them
a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))
avg = (a+b)/2
print("Average of numbers = ",avg)


#  Basic calculator

a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
addition = a+b
subtraction = a-b
multiplication = a*b
division = a/b
reminder = a%b
print("addition = ",addition)
print("subtraction = ",subtraction)
print("multiplication = ",multiplication)
print("division = ",division)
print("reminder = ",reminder)


# Rectangle  ---  Area and Parameter 

length = int(input("Enter the length = "))
width = int(input("Enter the width = "))
    # Area
Area = length * width
print("Area of Rectangle = ",Area)
    # Perimeter
Perimeter = 2*(length + width)
print("Perimeter of rectangle = ",Perimeter)


# Temperature Conversion
Celsius = int(input("Enter the tempature in Celsius = "))
Fahrenheit = (Celsius * (9/5)) + 32
print("Temperature in Fahrenheit = " , Fahrenheit)


# Swap two variables using 3rd variable
a = int(input("enter the value of a = "))
b = int(input("enter the value of b = "))
temp = a
a = b
b = temp
print ("a = ",a)
print("b = ",b)

#  swap of two numbers without using 3rd variable
a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))
a,b = b,a
print("a = ",a)
print("b = ",b)

# calculate the AGE
Present_YEAR = 2026
Birth_YEAR = int(input("Enter YOUR Birth YEAR = "))
AGE = Present_YEAR - Birth_YEAR
print("You are" , AGE, "Old")

# calculate the total Shopping bill 
a=int(input("Enter the value of a = "))
b=int(input("Enter the value of b = "))
c=int(input("Enter the value of c = "))
print ("Total Products sum = ",sum([a,b,c]))

#  average of three numbers
a=int(input("Enter the value of a = "))
b=int(input("Enter the value of b = "))
c=int(input("Enter the value of c = "))
print ("Total Products avg = ", sum([a,b,c])/len([a,b,c]))

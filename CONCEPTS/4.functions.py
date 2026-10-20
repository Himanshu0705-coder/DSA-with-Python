# Functions 

''' 
A function is a reusable block of code designed to perform a particular task.
'''

# Syntac Of FUNCTION

'''
def function_name(parameters):
    # block of code
    pass
'''

# Print first program using FUNCTION SYNTAX
def function():
    print("Hello Himanshu!")

function()


# addition of two numbers   -- function without parameter
A= int(input("Enter A's value :"))
B= int(input("Enter B's value :"))

def addition():
    sum = A+B
    print(sum)

addition()


# addition of two numbers   -- function with parameter
def addition(A,B):
    print(A+B)
addition(10,20)


# funtion with return
def addition(a,b):
    return a+b
result = addition(1,20)
print(result)



# multiple parameter
def student (name,age, marks):
    print(name , age)
    print(name , marks)
    print(age , marks)
student('Himanshu', 21 , 40)



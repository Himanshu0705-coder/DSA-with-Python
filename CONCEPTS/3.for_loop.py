# # for loop in python 

# '''
# for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string).
# OR
# for loop is used when you want to repeat a block of code for each item in a sequence/iterable.
# '''

# # syntax of for loop
# '''
# for (variable) in (sequence):
#     # block of code
#     pass
# '''


# # Loops
#     # for loop
#             # for i in range(start,stop,step):
    
#     # while loop
#     # do while loop


#  Print no. from 1 to 10
for i in range(1,11):
    print(i)

#  print no. from 10 to 1
for i in range (10,1,-1):
    print(i)

# print even no. from 1 to 50
for i in range(2,50,2):
    print(i)

#  print odd no. from 1 to 50
for i in range(1,50,2):
    print(i)

#  print multiple of 5 from 1 to 100
for i in range(5,100,5):
    print(i)
# OR
for i in range(1,100):
    if i % 5 == 0:
        print(i)

#  print the multiplication table
n= int(input("Enter the number : "))

for i in range(1,11):
    print (n , "x" , i , "= " , n*i)
    

#  Print square of the number from 1 to 10
for i in range (1,10):
    print(i*i)
# OR
#  If the range is not given 
n = int(input("Enter the value of n : "))
o = int(input("Enter the value of o : "))
for i in range(n,o):
    print(i*i)


#  Print cube of numbers from 1 to 10
for i in range(1,11):
    print(i*i*i)
# OR
n = int(input("Enter the value of n : "))
o = int(input("Enter the value of o : "))
for i in range(n,o):
    print(i*i*i)


# find the sum of number from 1 to N
N = int(input("enter the Value : "))
sum = 0 
for i in range (1,N+1):
    sum = sum +i
print(sum)


# Find the sum of even numbers from 1 to N
N = int(input("Enter the value of N :"))
sum = 0
for i in range(2,N +1,2):
    sum = sum +i
print("Sum of even numbers = " , sum)


# Find the sum of odd numbers from 1 to N
N = int(input("Enter the value :"))
sum = 0
for i in range(1, N+1 ,2):
    sum = sum + i
print("Sum of odd no. is ", sum)


# Count numbers divisible by 3
N = int(input("Enter the value :"))
count = 0
for i in range(1,N+1):
    if i % 3 == 0 :
        count = count + 1
print ("Count of no." , count)


# Count even and odd numbers
N = int(input("Enter the value :"))
even_count = 0
odd_count = 0
for i in range(1,N+1):
    if i % 2 == 0 :
        even_count += 1
        
    else:
        odd_count += 1
print ("Positive no. ", even_count)
print ("Odd number" , odd_count)


# Find the average of N numbers
M = int(input("Enter the starting value :"))
N = int(input("Enter the ending value :"))
average = 0
sum = 0
count = 0
for i in range (M,N+1):
    sum = sum + i
    count = count + 1
    average = sum/count
print("Sum of values :",sum)
print("Count of Values :",count)
print("Average of values :",average)



#  All questions are for LIST

# Find largest number in the list 
# Find the smallest number
# Find the sum of elements in a list
# Count positive, negative and zero
# Count numbers greater than 50
# Find the second largest number

# # What is Two pointer
# '''
# Two pointer technique means using two indexes/pointers to find the position of an array/linkList.
# '''
# # Where we use Two-Pointer concept/technique
# '''
# If somewhere is given or find   --

# i.   Array / LinkedList
# ii.  Sorted / Sort
# iii. Merger / Remove duplicate / rearrange
# iv.  Detect Cycle
# v.   Pair / Triplets / Qudrants
#  '''

# # most basic pattern to understand the Two-pointer concept
# '''
# left = 0
# right = len(arr) - 1

# while (left < right):
#     # Logic
    
#     if condition:
#         left += 1  yaa fir     left = left + 1
    
#     else:
#         right -= 1   yaa fir    right = right - 1
# '''


# # LEVEL 1 — Basic Two Pointer Questions

# #  example
# arr = [1,2,3,4,5]
# left = 0
# right = len(arr) - 1

# while (left < right):
#     print (arr[left] , arr[right])

#     left = left + 1
#     right = right - 1


# # print element from both end 
# arr = [10,20,30,40,50]
# left = 0
# right = len(arr) - 1

# while (left < right):
#     print (arr[left] , arr[right])

#     left = left + 1
#     right = right - 1



# # Reverse an array
# arr = [10,20,30,40,50,60]
# left = 0
# right = len(arr) - 1

# while (left < right):
#     arr[left],arr[right] = arr[right],arr[left]

#     left = left + 1
#     right = right - 1
# print(arr)



# #  check if an "Array" is palindrom
# # example 1
# arr = [1,2,3,4,5]
# left = 0
# right = len(arr) - 1

# while left < right :
#     if arr[left] != arr[right]:
#         print (arr , "is Not a Palindrom")
#         break

#     left = left + 1
#     right = right - 1

# else:
#     print(arr , " is Palindrom")

# # example 2

# num = list(map(int,input("enter the number :").split()))

# left = 0
# right = len(num) - 1

# while left < right :
#     if num[left] == num[right]:
#         print(num , "is in Palindrom")
#         break
#     left = left + 1
#     right = right - 1
# else:
#     print(num , "is not in Palindrom")



# #  check if an "String" is palindrom
# # example 1

# word = "Madam"
# left = 0
# right = len(word) -1

# while left < right :
#     if word[left] == word[right]:
#         print (word ," is Palindrom")
#         break
#     left = left + 1
#     right = right -1
# else:
#     print(word , "not a palindrom")

# # example 2

# name = input("Enter a name : ")

# left = 0
# right = len(name) - 1

# while (left < right) :
#     if name[left] == name[right]:
#         print(name , "is a palindrom")
#         break
#     left = left + 1
#     right = right - 1

# else:
#     print(name , "is not a palindrom")



# # Find the sum of first and last element
# # by given array
# num = [10,20,30,40]
# left = 0 
# right = len(num) - 1

# while left < right :
#     print ("The sum of first and last element is " ,num[left] + num[right])

#     left += 1
#     right -= 1

# #  by taking input values
# value = list(map(int,input("Enter the values ").split()))
# left = 0 
# right = len(value) - 1

# while left < right :
#     print(value[left] + value[right])

#     left += 1
#     right -= 1 






# # LEVEL 2 — Basic Interview Problems

# # Two sum -- Sorted Array
# # by given array
# arr = [10,20,30,40,50]
# target = 40
# left = 0
# right = len(arr) - 1

# while left < right:

#     if (arr[left] + arr[right] == target):
#         print("Pair found :", arr[left],arr[right])
#         break

#     elif (arr[left] + arr[right] < target):
#         left += 1

#     else:
#           right -= 1
# else:
#     print("No pair found")

# by input 
value = list(map(int,input("Enter the value :").split()))
target = int(input("Enter the target value :"))

left = 0 
right = len(value) - 1

while left < right :
    if value[left] + value[right] == target :
        print ("Target values :",value[left],value[right])
        break
    elif value[left] + value[right] < target :
        left += 1
    else:
        right -= 1
else:
    print("Invalid pair")


#  Count Pairs with a given sum  -- means pair of indexes whose sum are equal to the target  
arr = [10,20,30,40,50,60]
target = 80
left = 0
right = len(arr) - 1
count = 0
while left < right :
    total = arr[left] + arr[right]
    if total == target :
        print("Pair :",arr[left],arr[right])
        count += 1

        left += 1
        right -= 1

    elif total < target :
        left += 1
    else:
        right -= 1
print ("Total pairs:", count)


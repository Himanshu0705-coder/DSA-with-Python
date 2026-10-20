# print array elements using Two pointers 
array = [10,20,30,40,50,60]

left = 0
right = len(array) -1

while left < right :
    print(array[left],array[right])

    left += 1
    right -=1

    



# reverse the array 

array = [10,20,30,40,50]

left = 0 
right = len(array) - 1

while left < right :
    array[left], array[right] = array[right],array[left]

    left += 1
    right -= 1

print(array)





#  Level 1 - Palindrome
# check whether a string is palindrom or not 

string = "madam"

left = 0
right = len(string) - 1

while left < right :
    if string[left] == string[right]:
        print (True)
        break
    left +=1
    right -=1

else :
    print(False)




#  Level -2  ---- Find Pair with target sum

# find whether two numbers add up to a target

number = [10,20,30,40,50,60]

left = 0
right = len(number)-1
target = 50

while left < right :
    total = number[left] + number[right]

    if total == target:
        print(number[left],number[right])
        
        left += 1
        right -= 1
        
    elif total < target :
        left += 1

    else:
        right -= 1


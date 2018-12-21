'''

'''



"""
Method#1: Using Temp Array
Description
Algorithm:
Time Complexity : O(n)
Space Complexity: O(d)

"""

def arrayRotationTempArray(arr,d):
    tempArray =[]
##Step#1: if shift value greater than 0, reserve the values in temp array
    if d > 0:
        for i in range(d):
            tempArray.append(arr[i])
##Step#2: shift the remaining array to the left
    for i in range(d,len(arr)):
        arr[i-d] = arr[i]
##Step3: copy the temp array to the last indexes of main array
    for i in range(d):
        arr[len(arr) -(d -i) ] = tempArray[i]



"""
Method#2: rotate one by one
Description
Algorithm:
Time Complexity : O(d*n)
Space Complexity: O(1)

"""

def rotateOnebyOne(arr, d):
    for i in range(d):
        temp = arr[0]
        for j in range(len(arr) -1 ):
            arr[j] = arr[j+1]
        arr[len(arr) -1] = temp


"""
Method#3        : Reversal
Description     : Left rotation of Array using reversal method
Algorithm       :
Time Complexity : O(n)
Space Complexity: O(1)
"""

def reverseArray(arr, start, end):
    while(start < end ):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

def leftRotateReverese(arr, d):
    n = len(arr)
    if(d > n):
        shiftvalue = d % n
    else:
        shiftvalue = d
    reverseArray(arr, 0, shiftvalue -1)
    reverseArray(arr, shiftvalue, n-1 )
    reverseArray(arr, 0 , n-1)


"""
Method#4        : Pythonicway
Description     : Left rotation of Array using reversal method
Algorithm       :

get slice [x:y]	O(k)
del slice	O(n)
set slice	O(n+k)

Time Complexity : O(n)
Space Complexity: O(1)

"""


def rotateArrayPythonic(arr,d):
    print(arr[:d])
    print(arr[d:])
    return (arr[d:] + arr[:d])






#Driver Code

arr = [1,2,3,4,5,6]
#arrayRotationTempArray(arr,2)
#rotateOnebyOne(arr,2)
#leftRotateReverese(arr, 1078078071)
arr  = rotateArrayPythonic(arr,3)
print(arr)
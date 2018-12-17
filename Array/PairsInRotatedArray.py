'''
Problem1 ": Given a sorted and rotated array, find if there is a pair with a given sum.

'''


def findpair(arr, sum):
    length = len(arr)
    # find pivot index
    #Arguments: Low= 0th index, High= Length of array -1, Array
    #returns -1 if not found
    pivotIndex = findPivot(arr,0, length -1 )

    if pivotIndex == -1:
        l = 0
        r= length-1
    else:
        l = pivotIndex+1
        r = pivotIndex

    while l!= r:
        if arr[l] + arr[r] == sum:
            return True
        # 4,5,6,38,1,2,10
        if arr[l] + arr[r] < sum:
            l = (l+1) % length
        else:
            r= (r -1 + length) % length
    return False



def findPivot(arr, low, high):

    # Base Cases:
    #Base Case#1: Array is not reotated
    if high < low:
        return -1

    # Base Case#2: There is one element.
    if low == high:
        return low

    # Calculate mid to check neighbours
    mid = int((low + high)/2)

    if arr[mid] < arr[mid - 1]:
        return mid -1

    if arr[mid] > arr[mid + 1]:
        return mid

    if arr[low] <= arr[mid]:
        return findPivot(arr, mid+1, high )
    return findPivot(arr, low, mid)




# driver Code
arr = [3,4,5,6,7,1,2]

print (findpair(arr,3))

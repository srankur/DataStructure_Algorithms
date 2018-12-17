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



def findPivot(arr, low, high)


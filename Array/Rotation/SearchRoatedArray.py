"""
Algo List:
1- PivotBinarySearch : Searchs the the element in a Sorted Roated array in O(logn) time.
2- searchSortedRotated: Improved version of the above algo.
3- findMin:Finds the element in Sorted and roated array


"""


"""
Description: Search in sorted Rotated Array.
Method#1:
1- Find the pivot element
2- divide the array in two parts.
3- Binary search the relevant array

Time complexity:  O(logn)
Space Complexity: O(1)
"""

def PivotBinarySearch(arr, key):
    # Step#1: Find the index of pivot element
    length = len(arr)
    pivot = findPivotIndex(arr, 0, length )

    if pivot == -1:
        regBinarySearch(arr, 0, length, key)

    if arr[pivot] == key:
        return pivot

    # Step#2: ;divide the array
    # Search in left array
    if arr[0] <= key:
        return regBinarySearch(arr, 0, pivot- 1, key)
    return regBinarySearch(arr, pivot+1, length, key)


def findPivotIndex(arr, low, high):
    # base Cases
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((low + high)/2)

    if arr[mid] > arr[mid + 1]:
        return mid
    if arr[mid] < arr[mid -1]:
        return mid-1

    if arr[low] <= arr[mid]:
        return findPivotIndex(arr, mid+1, high)
    return findPivotIndex(arr, low, mid-1 )



def regBinarySearch(arr, low, high, key):
    # basecases
    if high < low:
        return -1

    mid = int((high +low)/2)

    if arr[mid] == key:
        return mid

    if arr[mid] >= key:
        return regBinarySearch(arr, low, mid -1, key)
    return regBinarySearch(arr, mid +1, high, key)



"""
Description: Search in rotated Array
Method#2: do a binary search in sorted array
Time Complecity: O(logn)
"""

def searchSortedRotated(arr, low, high, key):
    print("Entered: High %s, Low %s"%(high, low))
    # base Case:
    if high < low:
        return -1

    mid = int ((low+high)/2)
    if arr[mid] == key:
        return mid
    '''
    if arr[low] < arr[mid] and arr[low] <= key <= arr[mid]:
        return searchSortedRotated(arr, low, mid -1, key)
    return searchSortedRotated(arr, mid+1, high, key)
    '''

    # Case1: Array low..mid is sorted and key lies within
    if arr[low] <= arr[mid]:
        if arr[low] <= key < arr[mid]:
            return searchSortedRotated(arr, low, mid -1, key)
        else:
            return searchSortedRotated(arr, mid+1, high, key)
    # Case2: Array mid+1..high is sorted and key lies within
    if arr[mid ] < key <= arr[high]:
        return searchSortedRotated(arr, mid+1, high, key)
    else:
        return searchSortedRotated(arr, low, mid -1, key)





"""
Description: Find minimu element in the SOrted Roated array
Method#3: do a binary search in sorted array
How does it works: Find minimum does a recursive search for pivot element
Time Complecity: O(logn)
"""


def findMin(arr, low, high):
    # base Case:

    # Array is not roated at all
    if high < low:
        return arr[0]
    # Array has just one element
    if high == low:
        return arr[low]

    # Calculate min to comapre the neighbours
    mid = int((high + low)/2)

    if arr[mid] > arr[mid + 1]:
        return arr[mid +1]

    if arr[mid] < arr[mid -1]:
        return arr[mid]

    # decide to go left half or right half
    if arr[high] < arr[mid]:
        return findMin(arr, mid+1, high)
    return findMin(arr, low, mid -1)







# Driver Code

arr = [4,5,6,7,8,15, 18, 90, 1, 2,]

arr1 = [5, 6, 1, 2, 3, 4]
arr2 = [1, 2, 3, 4]
arr3 = [1]
arr4 = [1, 2]
arr5 = [2, 1]
arr6 = [5, 6, 7, 1, 2, 3, 4]
arr7 = [1, 2, 3, 4, 5, 6, 7]
arr8 = [2, 3, 4, 5, 6, 7, 8, 1]
arr9 = [3, 4, 5, 1, 2]
arr10 = [5,4,3,2,1]

Array = [arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9, arr10]


length = len(arr)

#index = PivotBinarySearch(arr, 11)
#index = searchSortedRotated(arr, 0, length -1, 2 )
#print("Index of the elemet is %s"%index)

for i in range(len(Array)):
   print ("Min of arr=%s is %s"% (i , findMin(Array[i], 0, len(Array[i]) - 1)))


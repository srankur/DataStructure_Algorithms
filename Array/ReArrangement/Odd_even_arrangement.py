
'''
Problem Description :  Rearrange array such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i
Given an array of n elements. Our task is to write a program to rearrange the array such that elements at even positions
are greater than all elements before it and elements at odd positions are less than all elements before it.

Approach :
Step#1: Basically it is slicing of "sorted" array into half.
Step#2: traverse the array Mid-> Low and Mid + 1 -> high
Step#3: fill the alternate position as per the problem statement

'''

def oddevenarrangement(arr):

    # Step1: Copy the original array into aux array
    auxarr = list(arr)
    if auxarr is arr:
        print("I am original")
    else:
        print("I am clone")

    length = len(arr)

    # Step2: Sort the Aux array
    auxarr.sort()

    # Step3: start copying ODD elements from AUX array to Original Array
    startindex = int(length/2-1)
    for i in range(0,length,2):
        arr[i] = auxarr[startindex]
        startindex -= 1

    # Step4: start copying Even elements from AUX array to Original Array
    startindex = int(length/2 )
    for i in range(1,length,2):
        arr[i] = auxarr[startindex]
        startindex += 1



# Driver Code
if __name__ == "__main__":
    arr = [1,2,3,4,6,5]
    arr1 = [1, 2, 1, 4, 5, 6, 8, 8]
    oddevenarrangement(arr1)
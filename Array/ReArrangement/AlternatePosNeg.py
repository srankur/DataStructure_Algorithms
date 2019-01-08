"""
Problem Description: Rearrange array in alternating positive & negative items with O(1) extra space
arrange Array in an alternate fashion such that every positive number is followed by negative and vice-versa.
"""

''' 
Approach1: Doesn't maintain the elements order 
1- Findout the length
2- Since neg Number need to start at 0th position, initialize variable negNumber as 0. 
   similarly PosNumber variable starts with 1st index
3- loop the array and ensure -ve values at the neg positions
4- loop the array and ensure +ve values at the pos positions 

'''

def rearrangePosneg(arr):
    # Step1: Find out the length
    length = len(arr)

    #Step2: Traverse array in two parts.
    #       part1 will ensure the negative number odd position
    #       part2 will ensure the positive number even position

    negnumber = 0
    posnumber = 1

    # Stay at negnumber position and swap the value if you find a negative
    for i in range(0,length):
        if arr[i] < 0 and negnumber < length:
            arr[i],arr[negnumber] = arr[negnumber],arr[i]
            print("arr[%s] => %s \t Negarr[%s] => %s" %(i, arr[i],negnumber, arr[negnumber] ))
            negnumber += 2

    # Stay at posnumber position and swap the value if you find a postive
    for i in range(1,length):
        if arr[i] >= 0 and posnumber < length:
            arr[i],arr[posnumber]= arr[posnumber],arr[i]
            posnumber += 2

    print(arr)





'''
Approach2: Doesn't maintain the order
    1- partition the array in quicksort way considering 0 as the Pivot element
    2- 
'''


def rearrangePosNegQuickSortway(arr):
    # step1: find the length of the array
    length = len (arr)
    
    negpos = 0
    # partition the array in the quick sort way
    for i in range(length):
        if arr[i] < 0:
            arr[negpos],arr[i] = arr[i],arr[negpos]
            negpos += 1
    
   # NegPos saves the last location of the neg element in the array now.
   # Start a loop from 0th and Negpos +1 (the postive number starts from here) and replace the alternate elements

    posLoc = negpos + 1
    startLoop = 1
    while posLoc < length:
       arr[startLoop],arr[posLoc] = arr[posLoc],arr[startLoop]
       posLoc += 1
       startLoop += 2
    print(arr)










# Driver code
if __name__ == "__main__":
    arr = [-5, 3,2, -1, -4, 5, -6,-1,  -2, 8, 9, -1, -4]
    #rearrangePosneg(arr)
    rearrangePosNegQuickSortway(arr)

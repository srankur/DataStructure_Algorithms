"""
Problem Description: Rearrange array in alternating positive & negative items with O(1) extra space
arrange Array in an alternate fashion such that every positive number is followed by negative and vice-versa.
"""

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

# Driver code
if __name__ == "__main__":
    arr = [-5, 3,2, -1, -4, 5, -6,-1,  -2, 8, 9, -1, -4]
    rearrangePosneg(arr)
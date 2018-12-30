'''
Description:  Rearrange an array such that arr[i] = i
Method#1:
Time complexity:  2*O(n)
Example Output :

Arr after Iter [1] and 0 pass = > [9, -1, 1, 2, 3, 4, 5, 6, 7, 8]
Arr after Iter [2] and 0 pass = > [8, -1, 1, 2, 3, 4, 5, 6, 7, 9]
Arr after Iter [3] and 0 pass = > [7, -1, 1, 2, 3, 4, 5, 6, 8, 9]
Arr after Iter [4] and 0 pass = > [6, -1, 1, 2, 3, 4, 5, 7, 8, 9]
Arr after Iter [5] and 0 pass = > [5, -1, 1, 2, 3, 4, 6, 7, 8, 9]
Arr after Iter [6] and 0 pass = > [4, -1, 1, 2, 3, 5, 6, 7, 8, 9]
Arr after Iter [7] and 0 pass = > [3, -1, 1, 2, 4, 5, 6, 7, 8, 9]
Arr after Iter [8] and 0 pass = > [2, -1, 1, 3, 4, 5, 6, 7, 8, 9]
Arr after Iter [9] and 0 pass = > [1, -1, 2, 3, 4, 5, 6, 7, 8, 9]
Arr after Iter [10] and 0 pass = > [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Arr after Iter [11] and 1 pass = > [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Arr after Iter [12] and 2 pass = > [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Arr after Iter [13] and 3 pass = > [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Arr after Iter [14] and 4 pass = > [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Arr after Iter [15] and 5 pass = > [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Arr after Iter [16] and 6 pass = > [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Arr after Iter [17] and 7 pass = > [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Arr after Iter [18] and 8 pass = > [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Arr after Iter [19] and 9 pass = > [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

def fixPosition(arr):
    length = len(arr)
    index = 0
    iter = 0
    # Step#1: Run a loop through the array to cover all the element
    while index < length:
        # Step#2: check if the corresponding index value isn't -1 or the index itself. 
        val = arr[index]
        iter += 1
        print("Arr after Iter [%s] and %s pass = > %s" % (iter, index, arr))
        if  val != -1 and val != index:
            # Step#3 : Swap and keep swapping the values till the index/values meet above criteria
            arr[val], arr[index] = arr[index], arr[val]

        else:
            index += 1


def fixPositionSet(arr):

    # Step#1: Create Set/dictionary
    arrset = set(arr)

    # Step#2: iterate through the set and check relative index postition in array for value
    for i in range(len(arr)):
        if i != -1 and i in arrset:
            arr[i] = i
        else:
            arr[i] = -1
    print(arr)





# Driver Code
if __name__ == "__main__":
    arr = [-1,-1, 6,1,9,2,3,-1,4,-1]
    arr1 = [9, -1, 1, 2, 3, 4, 5, 6, 7, 8]
    #fixPosition(arr1)
    fixPositionSet(arr)



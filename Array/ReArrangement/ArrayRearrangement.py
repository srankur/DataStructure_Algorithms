'''
Description:  Rearrange an array such that arr[i] = i
Method#1: 
'''

def fixPosition(arr):
    length = len(arr)
    index = 0
    # Step#1: Run a loop through the array to cover all the element
    while index < length:
        # Step#2: check if the corresponding index value isn't -1 or the index itself. 
        val = arr[index]
        if  val != -1 and val != index:
            arr[val], arr[index] = arr[index], arr[val]
        else:
            index += 1
        print("Arr after %s pass = > %s" %(index, arr))




# Driver Code
if __name__ == "__main__":
    arr = [-1,-1, 6,1,9,3,2,-1,4,-1]
    fixPosition(arr)



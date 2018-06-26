'''
##############################################################################
insertionSortKeySwap: replaces the key with each of previous bigger element
##############################################################################
'''


def insertionSortKeySwap(arr):
    ##loop over the array for its length
    for i in range(len(arr)):
        # j will be loop till the value of i i.e. for i = 4, j will run as 5,4,3,2,1
        for j in reversed(range(i)):
            if(arr[j+1] < arr[j]):
                #print("Inside if, Value of J",j)
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("Pass#",i,"::",arr )



''''
##############################################################################
#insertionSortSlideReplace: slides number to right and replace the key at    # 
#right positoion                                                            ##
##############################################################################
'''

def insertionSortSlideReplace(arr):
    print(arr)

arr = [7,5,8,4,78,-1,-2.5,6.7]

insertionSortKeySwap(arr)
#print(arr)
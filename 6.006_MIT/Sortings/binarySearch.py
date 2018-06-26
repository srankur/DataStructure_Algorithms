def binarySearchRec(arr,key ):
    mid = int(len(arr)/2)
    print("Mid is ", mid)

    if(key == arr[mid]):
        print(key, "is equal to",arr[mid] )
        return mid

    elif(key < arr[mid]):

        print(key, "is less  than", arr[mid], "Calling", arr[:mid])
        return mid + binarySearchRec(arr[:mid],key)

    elif (key > arr[mid]):
        print(key, "is greater than", arr[mid], "Calling", arr[mid + 1:])
        return mid + binarySearchRec(arr[mid + 1:],key)

    else:
        return -1

def BinarySearchiterative(arr, key):
    low = 0
    high = len(arr)
    # tow ways for mid
    # if want to have low left offset high+low/2
    # if do not want to have low left offset high - low/2
    #mid = high + low /2
    if 0 >= high:
        print("Nothing in given list")
        return
    while low < high:
        mid = int((high + low )/ 2)
        print("HIGH:",high,"MID:", mid,"LOW:", low)
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            low = mid+1
        elif key < arr[mid]:
            high = mid -1
        else:
            return


        
        

arr = [1,4,7,9,45,78,90]
arr1=[]
#index = binarySearchRec(arr, 90)
index = BinarySearchiterative(arr,-1)
print("index found::", index)



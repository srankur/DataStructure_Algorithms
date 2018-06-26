
def mergeArr(arr,leftArr,rightArr):

    print("Pre Merge Array::", arr)
    print("Pre Merge Left Arr:", leftArr)
    print("Pre Merge Right Arr:", rightArr)
    i=0
    j=0
    k=0

    while(i < len(leftArr)  and j < len(rightArr)):
        if(leftArr[i] < rightArr[j]):
            arr[k] = leftArr[i]
            i +=1
            k +=1
        elif( leftArr[i] > rightArr[j]):
            arr[k] = rightArr[j]
            j +=1
            k +=1

    while(i < len(leftArr)):
        arr[k] = leftArr[i]
        i += 1
        k += 1

    while (j < len(rightArr)):
        arr[k] = rightArr[j]
        j += 1
        k += 1
    print("Post Merge:",arr)




def mergeSort(arr):
    if (len(arr) == 1):
        print("List has one element, Must be sorted!!")
        return

    if(len(arr) > 1):
        mid = int(len(arr) / 2)
        leftArr = arr[:mid]
        rightArr = arr[mid:]

        print("Pre Split:", arr)
        print("Post Split, Left Arr:", leftArr)
        print("Post Split, right Arr:", rightArr)

        mergeSort(leftArr)
        mergeSort(rightArr)
        mergeArr(arr, leftArr, rightArr)
    else:
        print("EmptyList, Nothing to sort!! ")


arr = [76,45,89,34,90,-1,9.6,-2.55]
arr1= [34]
masterarr = [arr,arr1]

for i in masterarr:
    print("########################")
    print("Sorting List:", i)
    print("########################")
    mergeSort(i)
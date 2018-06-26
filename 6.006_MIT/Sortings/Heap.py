def MaxHeapify(arr,n,i):
    print("Inside Max heap")
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    print("ReceivedArray", arr)

    if (l < n  and arr[i] < arr[l]):
        largest = l
    if(r <n and arr[largest] < arr[r]):
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest], arr[i]
        print("Calling Max Heap with", arr,"largest",largest)
        MaxHeapify(arr,n,largest)
    print("exiting Max heap")

def buildMaxheap(arr,n):
    print("Inside BuildMax")
    for i in reversed(range(int(n/2))):
        print("Passed N, I",n,i)
        MaxHeapify(arr,n,i )
    print(arr)
    print("Exiting BuildMax")

arr = [ 12, 11, 13, 5, 6, 15]
#buildMaxheap(arr)

def heapSort(arr):
    n = len(arr)
    buildMaxheap(arr,n)
    print("Array after BuildMax",arr)

    for i in range(1,n):
        print("arr[0],arr[n-i],i", arr[0], arr[n - i], i)
        arr[0],arr[n-i] = arr[n-i],arr[0]
        #print("arr[0],arr[n-i],i", arr[0],arr[n-i],i)
        MaxHeapify(arr,n-i,0)
    print("Final Array::",arr)


heapSort(arr)
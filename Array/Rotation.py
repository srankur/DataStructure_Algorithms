def reverseArray(arr, start, end):
    while(start < end ):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1


def leftrotate(arr, d):
    n = len(arr)
    shiftvalue = 0
    if(d > n):
        shiftvalue = d % n
    else:
        shiftvalue = d
    reverseArray(arr, 0, shiftvalue -1)
    reverseArray(arr, shiftvalue, n-1 )
    reverseArray(arr, 0 , n-1)

arr = [1,2,3,4,5,6]
leftrotate(arr, 1078078078)
print(arr)
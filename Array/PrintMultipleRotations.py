'''
Description: find multiple left rotations of an array

Input : arr[] = {1, 3, 5, 7, 9}
        k1 = 1
        k2 = 3
        k3 = 4
        k4 = 6
Output : 3 5 7 9 1
         7 9 1 3 5
         9 1 3 5 7
         3 5 7 9 1

Input : arr[] = {1, 3, 5, 7, 9}
        k1 = 14
Output : 9 1 3 5 7


Approach#1: 1- make copy of the array
            2- Execute all the the iterations on the existing array.


Approach#2: 1- Execute the queries in a loop with k -> k + length time, loop will run exactly the the length of array
            2- print arr[i % n ]


'''



def printMultiRotation(arr, n, k ):
    for i in range(k, k+n):
        print(arr[i % n], end = " ")
    print()

# Driver code

arr = [1, 3, 5, 7, 9]
n = len(arr)
k = 2;
printMultiRotation(arr, n, k)

k = 3;
printMultiRotation(arr, n, k)

k = 4
printMultiRotation(arr, n, k)


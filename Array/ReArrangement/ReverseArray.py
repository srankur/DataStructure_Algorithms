'''
Description: Array/String Reversal.

'''

"""
Method#1: Iterative Method
Time complexity: O(n)
Space Complexity: O(1)
"""

def iterative_reversal(arr):
    length = len(arr)
    # Step-1: initialize variables start and end
    start = 0
    end = length -1
    # Step-2: run loop with below condition and keep swapping the variables
    while start < end:
        arr[start],arr[end] = arr[end], arr[start]
        # Step-3: increment the start and decrement the end variable
        start += 1
        end -= 1
    return arr


def recursive_reversal(arr, start , end):
    # Base condition
    if start >= end:
        return
    # Swap the elments and call the fucntion recursively
    arr[start], arr[end] = arr[end], arr[start]
    print(arr)
    recursive_reversal(arr, start + 1, end - 1)





# Driver code
if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    #print(iterative_reversal(arr))
    print(arr)
    recursive_reversal(arr, 0, len(arr) -1 )
    print (arr)
"""
Problem Description: Puss all zero to end in an array

"""

# Approach -1 :
# Step1 : Keep track of the Zero
# Step2 : Traverse the array
# Step3 : copy the array item at the count index if it non-zero
# Step4 : run a loop for leftover indexs to fill it with zero

def pushZerotoend(arr):
    # Step1: initialize a pointer which will keep track of the zero lies in between.
    count = 0

    # Step2: traverse the array
    for i in range(len(arr)):
        if arr[i] != 0:
            # This step saves un-necessary writes
            if arr[count] == arr[i]:
                count += 1
                print("No Write operation Needed")

            else:
                arr[count] = arr[i]
                print("Just wrote")
                count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1







# Driver Code

if __name__ == "__main__":
    arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
    arr1 = [1, 9, 8, 8, 4, 0, 0, 2,4, 7, 0, 6, 0, 9]
    pushZerotoend(arr1)
    print(arr1,sep=" ")

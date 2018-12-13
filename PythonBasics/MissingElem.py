# getMissingNo takes list as argument
'''
Explanation:
Truth Table for XOR
a | b | a ^ b
--|---|------
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0
Solution has:
1- X1 as XOR of all the element of Arrays i.e. X1 = A[0]^A[1]^A[2]^A[4]^A[5]
    X1 = 1^2^4^5^6
2- X2 as XOR of n+2 starting from A[0] t.e.
    X2 = 0^1^2^3^4^5^6
3- (X1^X2)  => (1^2^4^5^6) ^ (0^1^2^3^4^5^6)
            => (0)^(1^1)^(2^2)^(3)^(4^4)^(5^5)^(6^6)
            => 0 ^0^0^(3)^0 ^0^0
            => 3
'''
def getMissingNo(A):
    n = len(A)
    x1 = A[0]  # For xor of all the elements in array
    x2 = A[0]  # For xor of all the elements from A[0] to n+2
    for i in range(n):
        x1 ^= A[i]
    for i in range(n+2):
        x2 ^= i
    return x1 ^ x2
#1,2,4,5,6
#1,2,3,4,6

def getMissing(A):
    Midindex = int(len(A)/2)#(A[len(A)+A[0]])/2
    StartIndex = 0
    EndIndex = len(A)
    while StartIndex < EndIndex:
        if A[Midindex] == Midindex + A[0]:
            continue
        elif A[Midindex] < Midindex + A[0]:
            StartIndex = Midindex
            Midindex = (StartIndex + EndIndex) / 2
        elif A[Midindex] > Midindex + A[0]:
            EndIndex = Midindex
            Midindex = (StartIndex + EndIndex) / 2




    x1 = A[0]  # For xor of all the elements in array
    x2 = A[0]  # For xor of all the elements from A[0] to n+2
    for i in range(n):
        x1 ^= A[i]
    for i in range(n+2):
        x2 ^= i
    return x1 ^ x2

#
def getMissingNoExtraSpace(A):
    return next( (i+1 for i in range(len(A)) if A[i] ^(i+1) != 0),None)




# Driver program to test above function
A = [2,3,4,5]

miss = getMissingNoExtraSpace(A)

print("Missing Number from List:: %s" % miss)
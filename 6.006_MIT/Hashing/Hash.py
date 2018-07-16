
def hashStringPostitionWeight(str, tablesize):
    sum =0
    for i in range(len(str)):
        sum = sum + ord(str[i]) *(i+1)
    return sum % tablesize


tablesize = []

hashresult = hashStringPostitionWeight("cat", 10)
print(hashresult)

hashresult = hashStringPostitionWeight("bat", 10)
print(hashresult)

hashresult = hashStringPostitionWeight("tfdsdsf", 10)
print(hashresult)

hashresult = hashStringPostitionWeight("gdfgdfwwdfgdsgfdfgdfgdfgdfgdfgdf", 10)
print(hashresult)


print (hash('cat') %10)
print (hash(hash('cat')))

#tablesize[hashresult] = "cat"







# Python3 implementation of the
# above approach
 
# Function to print the output
def printTheArray(arr, n):
 
    for i in range(0, n):
        print(arr[i], end = " ")
     
    print()
 
# Function to generate all binary strings
def generateAllBinaryStrings(n, arr, i):
 
    if i == n:
        printTheArray(arr, n)
        return
 
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)
 
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)
 
 

n = 4
arr = [None] * n
print(arr)

 
generateAllBinaryStrings(n, arr, 0)
 
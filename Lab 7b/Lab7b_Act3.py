
# By submitting this assignment, I agree to the following:
    #   "Aggies do not lie, cheat, or steal, or tolerate those who do."
    #   "I have not given or received any unauthorized aid on this assignment."
    # Name:         Manisha Subrahmanya
    # Section:      566
    # Assignment:   Lab 7b - Act 2b
    # Date:         16 Oct, 2021

import math

templistA = []
templistB = []
total = []
diff = []
prod = []
magsumA = 0
magsumB = 0
prodsum = 0

A = input("Enter the elements for vector A: ")
B = input("Enter the elements for vector B: ")
A = A.split()
B = B.split()
for i in range(len(A)):
    A[i] = float(A[i])
    B[i] = float(B[i])
    
    # Finding the squares of each element in the lists
    tempA = math.pow(A[i] , 2)
    templistA.append(tempA)
    tempB = math.pow(B[i] , 2)
    templistB.append(tempB)
    
    # Finding the magnitude of vectors A and B
    magsumA = magsumA + templistA[i]
    magsumB = magsumB + templistB[i]
    magA = math.sqrt(magsumA)
    magB = math.sqrt(magsumB)
    
    # Finding A + B and A - B
    totalAB = A[i] + B[i]
    diffAB = A[i] - B[i]
    total.append(totalAB)
    diff.append(diffAB)
    
    # Finding the dot product
    prodAB = A[i] * B[i]
    prod.append(prodAB)
    prodsum = prodsum + prod[i]

# Final outputs
print("The magnitude of vector A is {:.4f}".format(magA))
print("The magnitude of vector B is {:.4f}".format(magB))
print("A + B is" , total)
print("A - B is" , diff)
print("The dot product is" , prodsum)

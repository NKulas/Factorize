#BruteForce
#Description: Finds factors of a number with a brute force approach
#Created by: Noah Kulas
#Created date: Jun 7 2020

import math

Number = int(input("Enter the number to factor: "))
Root = math.floor(math.sqrt(Number))

FactorsFound = 0
TotalOperations = 0

CandidateFactor = 1
while CandidateFactor <= Root:
    if Number % CandidateFactor == 0:
        print (CandidateFactor, Number / CandidateFactor)
        FactorsFound += 1
    TotalOperations += 1

    CandidateFactor += 1

if FactorsFound == 1:
    print ("Number is prime")
else:
    print("Number is composite")

print ("Total operations: " + str(TotalOperations))
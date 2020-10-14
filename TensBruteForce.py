#TensBruteForce
#Description: Finds factors of a number with a modified brute force approach that 
#only needs to try every tenth number
#Created by: Noah Kulas
#Created date: Jun 7 2020

#TODO Since possible primes are separated by alternating distances of 2 and 4,
#some ten steps can be eliminated
#Starting at the square root and working down may be quicker for larger numbers

import math
import MathHelpers

Number = int(input("Enter the number to factor: "))
RootByTen = math.floor(
    math.floor(
        math.sqrt(Number)
    )
    / 10
)

#Tails are the rightmost digit of the number
CandidateTails = []

i = 10
while i < 100:
    Column = i % 10
    Row = math.floor(i / 10)
    Rotation = (Row * Column) % 10

    if Rotation == MathHelpers.GetDigits(Number, 1):
        if not CandidateTails.__contains__(Row):
            CandidateTails.append(Row)
    i += 1

FactorsFound = 0
TotalOperations = 0

for Tail in CandidateTails:
    Multiplier = 0
    while Multiplier < RootByTen:
        CandidateFactor = (10 * Multiplier) + Tail
        #CandidateFactor = (20 * Multiplier) + Tail

        if (Number % CandidateFactor == 0):
            print(CandidateFactor, Number / CandidateFactor)
            FactorsFound += 1

        TotalOperations += 1
        Multiplier += 1

if FactorsFound == 1:
    print ("Number is prime")
else:
    print("Number is composite")

print ("Total operations: " + str(TotalOperations))
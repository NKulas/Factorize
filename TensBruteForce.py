#TensBruteForce
#Description: Finds factors of a number with a modified brute force approach that 
#only needs to try every tenth number
#Created by: Noah Kulas
#Created date: Jun 7 2020

import numpy
import math

Number = int(input("Enter the number to factor: "))
RootByTen = math.floor(
    math.floor(
        math.sqrt(Number)
    )
    / 10
)

CandidateFactorLeads = numpy.empty(shape=0)

i = 10
while i < 100:
    Row = i % 10
    Column = math.floor(i / 10)
    Rotation = (Row * Column) % 10

    if (Number - Rotation) % 10 == 0:
        CandidateFactorLeads = numpy.append(CandidateFactorLeads, Row)
    i += 1

FactorsFound = 0
TotalOperations = 0

for CandidateLead in CandidateFactorLeads:

    CandidateFactorMultiplier = 0
    while CandidateFactorMultiplier <= RootByTen:
        CandidateFactor = (10 * CandidateFactorMultiplier) + CandidateLead

        if Number % CandidateFactor == 0:
            print(CandidateFactor, Number / CandidateFactor)
            FactorsFound += 1
        TotalOperations += 1

        CandidateFactorMultiplier += 1

if FactorsFound == 1:
    print ("Number is prime")
else:
    print("Number is composite")

print ("Total operations: " + str(TotalOperations))
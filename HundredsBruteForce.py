#HundredsBruteForce
#Description: Finds factors of a number with a modified brute force approach that 
#only needs to try every hundreth number
#Created by: Noah Kulas
#Created date: Jul 19 2020

import math

Number = int(input("Enter the number to factor: "))
RootByHundred = math.floor(
    math.floor(
        math.sqrt(Number)
    )
    / 100
)


#Tails two rightmost digits of a number
CandidateTails = []

Row = 0
while Row < 10:
    Column = 0
    while Column < 100:
        Rotation = (Row * Column) % 100

        if (Number - Rotation) % 10 == 0:
            Final = 0

            if Row > Column:
                Final = Row
            else:
                Final = Column
            
            if not CandidateTails.__contains__(Final):
                CandidateTails.append(Final)
        
        Column += 1
    Row += 1

TotalOperations = 0

for Tail in CandidateTails:
    Multiplier = 0

    while Multiplier < RootByHundred:
        CandidateFactor = (100 * Multiplier) + Tail

        if (Number % CandidateFactor == 0):
            print (CandidateFactor, Number / CandidateFactor)
        
        Multiplier += 1
        TotalOperations += 1

print("TotalOperations: " + str(TotalOperations))
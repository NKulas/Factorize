#Name: StepUpBruteForce
#Description: Finds factors of a number by trying a bunch of possibilites, and carrying the viable ones to the next round,
#with place value of numbers increasing in each round
#Created by: Noah Kulas
#Created date: October 1 2020

import math
import MathHelpers

OriginalNumber = int(input("Enter the number to factor: "))

def MatrixCompute(RoundIndex, StartingPoint):
    CandidateTails = []
    End = pow(10, RoundIndex)

    Row = StartingPoint[0]
    while Row < End:
        Column = StartingPoint[1] 
        while Column < End:

            FullRotation = Row * Column
            Rotation = FullRotation % End

            if Rotation == MathHelpers.GetDigits(OriginalNumber, RoundIndex):
                resultList = [Row, Column]
                resultList.sort()
                if not CandidateTails.__contains__(resultList):
                    CandidateTails.append(resultList)

            Column += pow(10, RoundIndex - 1)
        Row += pow(10, RoundIndex - 1)
    return CandidateTails

Operations = 0
Round = 1
Candidates = [[1,1]]
while True:
    NewCandidates = []
    for item in Candidates:
        Operations += 1
        if item[0] * item[1] == OriginalNumber:
            print(item[0], item[1])
            print("Total operations: " + str(Operations))
            exit()
        
        #I know this is repeated code, will fix eventually
        if item[0] != 1 and OriginalNumber % item[0] == 0:
            print(item[0], OriginalNumber / item[0])
            print("Total operations: " + str(Operations))
            exit()
        
        if item[1] != 1 and OriginalNumber % item[1] == 0:
            print(item[1], OriginalNumber / item[1])
            print("Total operations: " + str(Operations))
            exit()
        
        NewCandidates += MatrixCompute(Round, item)
    
    Candidates = NewCandidates
    Round += 1
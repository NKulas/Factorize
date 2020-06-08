#Diophantine
#Description: Provides functions for calculations related to Diophantine equations
#Created by: Noah Kulas
#Created date: May 22 2020

import math

#Find the greatest common factor of two numbers with the Euclidean algorithm
def EuclideanAlgorithm(First, Second, ReturnSteps):
    StepList = []

    if (Second > First):
            Temporary = First
            First = Second
            Second = Temporary

    while True:
        Remainder = First % Second

        if ReturnSteps:
            StepList.append(First)
            StepList.append(math.floor(First / Second))
            StepList.append(Second)
            StepList.append(Remainder)

        if Remainder == 0:
            if ReturnSteps:
                return StepList
            else:
                return Second
        else:
            First = Second
            Second = Remainder

#Used for addition in the Diophantine solving function
def Add(First, Second):
    SemiFirst = First
    if First < 0:
        SemiFirst = abs(First)

    SemiSecond = Second
    if Second < 0:
        SemiSecond = abs(Second)
    
    SemiFirst += SemiSecond

    if First < 0:
        SemiFirst *= -1
    
    return SemiFirst

#Find a solution to a diophantine equation
def DiophantineSolver(StepList, RequestedTotal):
    #Jump back to the last step without a remainder
    i = len(StepList) - 8

    RunningTotal = StepList[i + 3]

    RunningACoefficient = 1
    RunningAValue = StepList[i]

    RunningBCoefficient = StepList[i + 1] * -1
    RunningBValue = StepList[i + 2]

    i -= 4

    while i >= 0:
        StepTotal = StepList[i]
        StepFirst = StepList[i + 1] * -1
        StepSecond = StepList[i + 2]
        StepRemainder = StepList[i + 3]

        #See https://www.wikihow.com/Solve-a-Linear-Diophantine-Equation to understand what is being done here
        if RunningAValue == StepRemainder:
            RunningAValue = Add(RunningAValue, StepFirst * StepSecond)
            RunningBCoefficient = Add(RunningBCoefficient, RunningACoefficient * StepFirst)

        elif RunningBValue == StepRemainder:
            RunningBValue = Add(RunningBValue, StepSecond)
            RunningACoefficient = Add(RunningACoefficient, RunningBCoefficient)

        i -= 4

    Multiplier = RequestedTotal / RunningTotal
    #Rotate some things
    return (RunningAValue,
    RunningACoefficient * Multiplier, 
    RunningBValue,
    RunningBCoefficient * Multiplier,
    RunningTotal * Multiplier)

#Find greatest common factor of any number of numbers
def FindGcf(Numbers):
    FoundGcf = False

    while not FoundGcf:
        FoundGcf = True
        CommonFactors = []

        i = 0
        while i < len(Numbers):
            CommonFactors.append(
                EuclideanAlgorithm(
                    Numbers[i],
                    Numbers[(i + 1) % len(Numbers)],
                    False
                )
            )

            if len(CommonFactors) > 1:
                if Numbers[len(CommonFactors) - 1] != Numbers[len(CommonFactors) - 2]:
                    FoundGcf = False

            i += 1
        
        if FoundGcf:
            return CommonFactors[0]
        else:
            Numbers = CommonFactors

#Find least common multiple
def FindLcm(Numbers):
    Multiple = FindGcf(Numbers)
    Product = 1

    for Number in Numbers:
        Product *= Number
    
    return Product / Multiple
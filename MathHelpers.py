#MathHelpers
#Description: Some mathematical functions to assist with calculations needed in factoring
#Created by: Noah Kulas
#Created date: October 1 2020

import math

def DigitCount(inputNumber):
    i = 0
    while True:
        if inputNumber / pow(10, i) < 1:
            return i
        else:
            i += 1

def GetDigits(inputNumber, digitsWanted):
    digitCount = DigitCount(inputNumber)

    while digitCount > digitsWanted:
        inputNumber = inputNumber % pow(10, digitCount - 1)
        digitCount -= 1
    
    return inputNumber

def GetDigitsFromLeft(inputNumber, digitsWanted):
    digitCount = DigitCount(inputNumber)
    result = 0

    while digitsWanted > 0:
        divisor = pow(10, digitCount - 1)
        singleDigit = math.floor(inputNumber / divisor) 
        result += singleDigit * pow(10, digitsWanted - 1)
        inputNumber -= divisor * singleDigit
        digitsWanted -= 1
        digitCount -= 1
    
    return result
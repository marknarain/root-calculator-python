import math
from bignumber import *

# Splits the entered number into pairs of two digits.
# x = 1234 --> [12, 34]
# x = 123  --> [1, 23]
# x = 7    --> [7]
# The lenght of the resulting array == number of integer 
# digits of the square root of x
 
def splitNumber(x):

    output = [0]

    while x > 0:
        
        output[0] = x % 100
        x = (x - output[0]) / 100     
        if x == 0:
            break
        output.insert(0, 0)

    return(output)

# Finds the root of the closest smaller square number.
# x = 91    --> 9
# x = 64    --> 8
# x = 10    --> 3
# Entered values must be < 100

def rootOfFirstItem(x):
    y = 9
    while x < (y*y):
        y = y - 1

    return(y)

# Subtracts the square of the first found Digit from the entered number

def firstStepSquareMinus(x, y):
    output = x - y*y

    return(output)

# Uses a number x and the first found digit of the root
# to calculate the next root.

def rootDigitCalculator(x, y):

    #print(x)

    b = int(x / (20*y))
    
    x2 = BigNumber(x)

    y2 = BigNumber(y)

    b2 = BigNumber(b)

    a = BigNumber(20)

    while (a*y2*b2 + b2*b2) > x2:
        b2 = b2 - BigNumber(1)

    #while cmp(add((mul(mul(y2,b2),cnv(20))),mul(b2,b2)),x2) == 1:
    #    b2 = sub(b2,[1,1])
 
    #while (20*y*int(b)) + int(b)*int(b) > x:
    #    b = b - 1

    #assert b == arrayToInt(b2),arrayToInt(b2)

    #return(arrayToInt(b2.data))
    return (int(b2))

# Calculates the root of number a and returns it as text
# the parameter decimalPlaces defines how many decimal places after the comma
# should be calculated.

def root(a, decimalPlaces, debug = False):

    outputString = ""
    if a > 0:   
        aSplit = splitNumber(a)
        b = rootOfFirstItem(aSplit[0])
        outputString = outputString + str(b)
        c1 = firstStepSquareMinus(aSplit[0], b)*100

        d1 = 0
        x = 0
        lenA = len(aSplit)
        y = 1
        
        #-1 bacuse 1st digit is already calculated with rootOfFirstItem()
        totalPlaces = decimalPlaces +  len(aSplit) -1  

        while x+1 <= (totalPlaces):

            if debug == True:
                if x%100 == 0:
                    print(int((x/100)%10),end="")

            if lenA > 1:
                c1 = c1 + aSplit[x+1]
                lenA = lenA - 1
            b = int(b*y + int(d1*y/10) + int(d1*y/100))
            
            if (math.floor(math.log10(b))+1) == len(aSplit):
                outputString = outputString + (",")
            
            d1 = rootDigitCalculator(int(c1), b)
            outputString = outputString + str(d1)

            c1 = int((c1 - (20 * b * d1 + d1 * d1))*100)
            if c1 == 0:
                break
            
            x = x+1
            y = 10

    elif a < 0:
        outputString = outputString + ("")

    else:
        outputString = outputString + str(0)
    return(outputString)


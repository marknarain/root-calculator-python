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
    while x < (y**2):
        y = y - 1

    return(y)

# Subtracts the square of the first found Digit from the entered number

def firstStepSquareMinus(x, y):
    output = x - y**2

    return(output)

# Uses a number x and the first found digit of the root
# to calculate the next root.

def rootDigitCalculator(x, y):

    a = y*20
    b = x // a
    a += b
    
    while (a*b) > x:
        b -= 1
        a -= 1

    return b

# Calculates the root of number a and returns it as text
# the parameter decimalPlaces defines how many decimal places after the comma
# should be calculated.

def root(a, decimalPlaces):
    
    if a == 0:
        return "0"

    elif a < 0:
        assert False, "negative numbers not allowed!!!"

    outputString = ""
     
    aSplit = splitNumber(a)
    b = rootOfFirstItem(aSplit[0])
    outputString = outputString + str(b)
    c1 = firstStepSquareMinus(aSplit[0], b)*100

    d1 = 0
    lenA = len(aSplit)
    first = 1
    
    #-1 bacuse 1st digit is already calculated with rootOfFirstItem()
    x = decimalPlaces + lenA -1  

    while x > 0:

        x -= 1

        if lenA > 1:
            c1 += aSplit[x +1]
            lenA -= 1

        if first == 0:
            b *= 10

        first = 0

        b += d1
        
        d1 = rootDigitCalculator(c1, b)

        outputString = outputString + str(d1)

        c1 = (c1 - ((20 * b + d1) * d1)) *100
        if c1 == 0:
            break

    return outputString[:lenA] + "," + outputString[lenA:]
import math

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

    b = x / (20*y)
    
    while (20*y*int(math.floor(b)) + int(math.floor(b))*int(math.floor(b))) > x:
        b = b - 1

    return (int(b))

# Calculates the root of number a and returns it as text
# the parameter decimalPlaces defines how many decimal places after the comma
# should be calculated.

def root(a, decimalPlaces):

    
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

##################
## Main program ##
##################


inputNumberState = False
while inputNumberState == False:
    inputNumber = input("Enter your number: ")
    if inputNumber.isnumeric() == True:
        inputNumber = int(inputNumber)
        inputNumberState = True
    elif inputNumber == "":
        print("Your input was empty")
    else:
        print("Your input was invalid")

outputDigitsState = False

while outputDigitsState == False:

    outputDigitsPromt = "How many decimal places do you want to see (maximum {}): "
    outputDigitsPromt = outputDigitsPromt.format(309-2*len(splitNumber(int(inputNumber))))
    outputDigits = input(outputDigitsPromt)

    if outputDigits.isnumeric() == True:

        if int(outputDigits) <= (309-2*len(splitNumber(int(inputNumber)))):
            outputDigits = int(outputDigits)
            outputDigitsState = True
        else:
            digitsToBigOut = "The number of decimal places is bigger than {}"
            digitsToBigOut = digitsToBigOut.format((309-2*len(splitNumber(int(inputNumber)))))
            print(digitsToBigOut)

    elif outputDigits == "":
        confirm = input("Your input was empty, please confirm if you want to continue with 0 decimal places (Y): ")

        if confirm == "Y" or confirm == "y":
            outputDigits = "0"
            outputDigitsState = True

    else:
        print("Your input was invalid")



outText = root(inputNumber, outputDigits)

if outText == "":
    outText = "This function isn't avalible yet!"

else:
    outText = "The sqrt() of " + str(inputNumber) + " (" + str(outputDigits) + " decimal places) is: " + str(outText)


print(outText)

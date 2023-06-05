import time
import keyboard     # call pip install keyboard
import matplotlib.pyplot as plt    # call 'pip install matplotlib'

# Splits the entered number into pairs of two digits.
# x = 1234 --> [12, 34]
# x = 123  --> [1, 23]
# x = 7    --> [7]
# The lenght of the resulting array == number of integer 
# digits of the square root of x
 
def splitNumber(x):

    output = [0]

    while x > 0:
        
        output[0] = x %100
        x = (x - output[0]) /100     
        
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

    a = y *20
    b = x // a
    a += b
    
    while (a*b) > x:
        b -= 1
        a -= 1

    return b

# Calculates the root of number a and returns it as text
# the parameter decimalPlaces defines how many decimal places after the comma
# should be calculated.

keyPressed = False
graphArrayX = []
graphArrayY = []

def root(a, decimalPlaces, debug = False, outputFile = ""):
    
    global keyPressed
    f = open(outputFile + ".info.txt", 'w')
    f.write("")
    f.close()


    def on_key_event(event):
        # Process the key event
        global keyPressed
        keyPressed = True

    if debug == True:
        keyboard.on_press(on_key_event)

    if a == 0:
        return "0"

    elif a < 0:
        assert False, "negative numbers not allowed!!!"

    outputString = ""
    
    aSplit = splitNumber(a)
    b = rootOfFirstItem(aSplit[0])
    outputString = outputString + str(b)
    c1 = firstStepSquareMinus(aSplit[0], b) *100

    d1 = 0
    lenA = len(aSplit)
    first = 1
    
    #-1 bacuse 1st digit is already calculated with rootOfFirstItem()
    x = decimalPlaces + lenA -1
    startX = x

    tStart = int(time.time())
    tNext = tStart +10
    
    tenSecs = False
    firstWrite = 1

    while x > 0:
     
        if debug == True:
            
            if keyPressed == True:
                x = 0
            
        if time.time() > tNext:
            if outputFile != "":
                f = open(outputFile + ".info.txt", 'a')
                f.write("In " + str(tNext - tStart) + " seconds : " + str(startX - x) + " digits calculated\n")
                f.close()
                
                f = open(outputFile + ".txt", 'a')
                
                if firstWrite == 1:
                    outputString = outputString[:lenA] + "," + outputString[lenA:]
                    firstWrite == 0

                f.write(outputString)
                outputString = ""
                f.close()
            
            if debug == True:
                print("In " + str(tNext - tStart) + " seconds : " + str(startX - x) + " digits calculated")
                
                graphArrayY.append(tNext - tStart)
                graphArrayX.append(startX - x)

            tNext += 10
            tenSecs = True

        x -= 1

        if lenA > 1:
            c1 += aSplit[x +1]
            lenA -= 1

        if first == 0:
            b *= 10

        first = 0

        b += d1
        
        d1 = rootDigitCalculator(c1, b)

        outputString += str(d1)

        c1 = (c1 - ((20 * b + d1) * d1)) *100
        
        if c1 == 0:
            break

    if debug == True:
        plt.plot(graphArrayX,graphArrayY)
        plt.show()
        keyboard.unhook_all()
    
    if outputFile != "" and tenSecs == True:
        f = open(outputFile + ".txt", "a")
        f.write(outputString)
        f.close()
        return ""
    
    else:
        f = open(outputFile + ".txt", "w")
        f.write(outputString)
        f.close()
        return outputString[:lenA] + "," + outputString[lenA:]
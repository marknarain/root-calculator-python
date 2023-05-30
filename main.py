from root import *

###############################################
#
# Main program 
#
###############################################

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
    outputDigitsPromt = outputDigitsPromt.format(4200-2*len(splitNumber(int(inputNumber))))
    outputDigits = input(outputDigitsPromt)

    if outputDigits.isnumeric() == True:
        
        outputDigits = int(outputDigits)
        outputDigitsState = True

        if int(outputDigits) <= (4200-2*len(splitNumber(int(inputNumber)))):
            outputDigits = int(outputDigits)
            outputDigitsState = True
        else:
            digitsToBigOut = "The number of decimal places is bigger than {}"
            digitsToBigOut = digitsToBigOut.format((4200-2*len(splitNumber(int(inputNumber)))))
            print(digitsToBigOut)

    elif outputDigits == "":
        confirm = input("Your input was empty, please confirm if you want to continue with 0 decimal places (Y): ")

        if confirm == "Y" or confirm == "y":
            outputDigits = "0"
            outputDigitsState = True

    else:
        print("Your input was invalid")




outText = root(inputNumber, outputDigits, True)

if outText == "":
    outText = "This function isn't avalible yet!"

else:
    outText = "The sqrt() of " + str(inputNumber) + " (" + str(outputDigits) + " decimal places) is: " + str(outText)


print(outText)

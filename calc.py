def cmp(x, y):
    
    if x == y:
        output = 0
    elif x[0] > y[0]:
        output = 1
    elif x[0] < y[0]:
        output = -1
    else:
        if len(x) > len(y):
            if x[0] == 1:
                output = 1
            else:
                output = -1
        elif len(x) < len(y):
            if x[0] == 1:
                output = -1
            else:
                output = 1
        else:
            
            different = False
            output = 0
            whileCounter = 1

            while different == False:

                if x[whileCounter] > y[whileCounter]:
                    different = True
                    if x[0] == -1 and y[0] == -1:
                        output = -1
                    else:    
                        output = 1
                elif x[whileCounter] < y[whileCounter]:
                    different = True
                    if x[0] == -1 and y[0] == -1:
                        output = 1
                    else:    
                        output = -1
                else:
                    whileCounter = whileCounter + 1
                    if whileCounter > len(x)-1 or whileCounter > len(y)-1:
                        output = 0 
                        break

    return(output)





def plus(x, y):

    outputString = []
    carryOnNum = 0
    whileCounter = 1

    if x[0] == -1 and y[0] == 1:
        outputString = minus(y, x)

    elif x[0] == -1 and y[0] == -1:
        outputString = minus(x, y)
    
    elif x[0] == 1 and y[0] == -1:
        y[0] = 1
        outputString = minus(x, y)

    else: 
        outputString[0] = 1

        while len(x) > len(y):
            y.insert(1, 0)

        while len(y) > len(x):
            x.insert(1, 0)
        
        while (len(x) - whileCounter) >= 0: 

            digit = x[len(x)-whileCounter] + y[len(y)-whileCounter] + carryOnNum
            if digit > 9:
                carryOnNum = int((digit - digit % 10)/10)
                digit = digit % 10
                if carryOnNum > 0:
                    x.insert(1, 0)
                    y.insert(1, 0)
                outputString.insert(0, digit)
            
            else:
                outputString.insert(0, digit)
                carryOnNum = 0

            whileCounter = whileCounter + 1

    

    return outputString
    
#print(plus([2,2], [9]))
#print(plus([1], [9,2]))
#print(plus([1], [9,2,5]))
#print(plus([1], [9,2,5,6]))
#print(plus([1], [9,2,5,2,4]))
#print(plus([1], [1]))
#print(plus([3,4], [1]))
#print(plus([9,9,9], [1]))
#print(plus([1,9,2,4], [1]))
#print(plus([1,3,4,5,7], [1]))
#print(plus([9,1,2,3,5,5], [9]))
#print(plus([9,2], [9,2]))
#print(plus([9,2,5], [9,2,5]))
#print(plus([9,9,9,9], [9,2,5,6]))
#print(plus([1,1,2,3,4], [9,2,5,2,4]))






def minus(x, y):

    outputString = []
    carryOnNum = 0
    whileCounter = 1

    if x[0] == 1 and y[0] == -1:
        y[0] = 1
        outputString = plus(x, y)

    if x[0] == -1 and y[0] == -1:
        y[0] = 1
        outputString = minus(y, x)

    if x[0] == -1 and y[0] == 1:
        x[0] = 1
        outputString = plus(x, y)
        outputString[0] = -1

    else:
        if cmp(x, y) == -1:
            outputString = minus(y, x)
            outputString[0] = -1

        while len(x) > len(y):
            y.insert(1, 0)

        while len(y) > len(x):
            x.insert(1, 0)

        while (len(x) - whileCounter) >= 0: 
            
            digit = x[len(x)-whileCounter] - y[len(y)-whileCounter] - carryOnNum
          
            if digit < 0:
                carryOnNum = 1
                outputString.insert(1, digit*(-1))          

            else:
                carryOnNum = 0
                outputString.insert(0, digit)

            whileCounter = whileCounter + 1



    return(outputString)


#print(minus([9,2], [9,4]))
#print(minus([1], [9]))
#print(minus([2], [9,2]))
#print(minus([3], [9,2,5]))
#print(minus([4], [9,2,5,6]))
#print(minus([5], [9,2,5,2,4]))
#print(minus([1], [1]))
#print(minus([3,4], [1]))
#print(minus([9,9,9], [1]))
#print(minus([1,9,2,4], [1]))
#print(minus([1,3,4,5,7], [1]))
#print(minus([9,1,2,3,5,5], [9]))
#print(minus([9,2], [9,2]))
#print(minus([9,2,5], [9,2,5]))
#print(minus([9,9,9,9], [9,2,5,6]))
#print(minus([1,1,2,3,4], [9,2,5,2,4]))

#print(minus(['-',1,1,2,3,4], [9,2,5,2,4]))






def multi(x, y):
     
    number1 = [int(i) for i in str(x)]
    number2 = [int(i) for i in str(y)]

    outputString = []
    carryOnNum = 0
    x = 1


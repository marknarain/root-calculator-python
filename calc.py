def cmp(x, y):
    
    if x[0] > y[0]:
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

def add(x, y):

    output = []
    carryOnNum = 0
    whileCounter = 1
  
    if x[0] == -1 and y[0] == 1:
        output = add(y,x)

    elif x[0] == -1 and y[0] == -1:
        x[0] = 1
        y[0] = 1
        output = add(x, y)
        output[0] = -1
   
    else: 
        output.insert(0,1)

        while len(x) > len(y):
            y.insert(1, 0)

        while len(y) > len(x):
            x.insert(1, 0)
                
        while ((len(x)-1) - whileCounter) >= 0: 
                        
            if x[0] == 1 and y[0] == -1:
                y[0] = 1
                if cmp(x,y) == -1:
                    x[0] = -1
                    output = add(y,x)
                    output[0] = -1
                    break
                y[0] = -1

                digit = x[len(x)-whileCounter] - y[len(y)-whileCounter] - carryOnNum
                if digit < 0:
                    carryOnNum = 1
                    output.insert(1, digit+10)
                else:    
                    carryOnNum = 0
                    if ((len(x)-1) - whileCounter) == 0 and x[1] == y[1]:
                        if len(x) == 2:
                            output.insert(1, 0)
                        break
                    else:
                        output.insert(1, digit)
                whileCounter = whileCounter + 1        

            else:
                digit = x[len(x)-whileCounter] + y[len(y)-whileCounter] + carryOnNum
                if digit > 9:
                    carryOnNum = int((digit - digit % 10)/10)
                    digit = digit % 10
                    output.insert(1, digit)
                else:
                    output.insert(1, digit)
                    carryOnNum = 0

                whileCounter = whileCounter + 1
                if carryOnNum > 0 and len(x)-whileCounter == 0:
                    output.insert(1,carryOnNum)

    if output == [-1,0]:
        output[0] = 1

    return output

def sub(x,y):
    y[0] = y[0]*(-1)
    res = add(x,y)
    y[0] = y[0]*(-1)
    return(res)

def mul(x, y):
     
    carryOnNum = 0
    whileCounter1 = 1
    whileCounter2 = 1    
    output = [1,0]
    mullAdd = [1]

    if len(x) == 2 and len(y) > len(x):
        output = mul(y,x)
    
    else:

        while ((len(y)-1) - whileCounter1) >= 0:

            while ((len(x)-1) - whileCounter2) >= 0:
                digit = y[1] * x[len(x)-whileCounter2] + carryOnNum
                carryOnNum = int(digit/10)
                mullAdd.insert(1,digit%10)
                whileCounter2 = whileCounter2 + 1

            output = add(output,mullAdd)
            if ((len(y)-1) - whileCounter1) != 0:
                output.append(0)
            

            if ((len(y)-1) - whileCounter1) <= 0:
                output.insert(1,carryOnNum)
                break
               
            whileCounter1 = whileCounter1 + 1

        if x[0] != y[0]:
            output[0] = -1
    
    return(output)

def div(x,y):
    if y == [1,1,0]:
        x.pop(1)
        output = x 
    elif y == [1,1,0,0]:
        x.pop(1)
        x.pop(1)
        output = x
    else:
        assert output == "Not yet Avalible"

    return(output)

def cnv(x):
    positiveX = x
    if x < 0:
        positiveX = positiveX * (-1)

    output = [int(i) for i in str(positiveX)]
    if x >= 0:
        output.insert(0,1)
    else:
        output.insert(0,-1)

    return(output)

def stringCnv(x):
    whileCounter = 1
    output = ""
    if x[0] == -1:
            x.pop(0)
            output = output + "-"
    else:
        x.pop(0)

    while len(x) - whileCounter >= 0:
        output = output + str(x[whileCounter-1])
        whileCounter = whileCounter +1

    return(output)

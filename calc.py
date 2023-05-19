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
    return(add(x,y))

def mul(x, y):
     
    output = []
    carryOnNum = 0
    x = 1


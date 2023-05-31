class BigNumber():

    data = []
    packLength = 10**5000

    def __init__(self,value):
        if type(value) is int:
            packs = []
            negative = False
            if value < 0:
                packs.append(-1)
                value = value*(-1)
                negative = True
            else:
                packs.append(1)
            while value != 0:
                modNum = value % self.packLength
                packs.insert(1, modNum)
                value = (value - modNum) // self.packLength

            if negative == True:
                value = value*(-1)
            
            if packs == [1]:
                packs = [1,0]
            self.data = packs

        else:
            self.data = value

    def __add__(self,other):

        newObject = BigNumber(0)
        
        output = []
        carryOnNum = 0
        whileCounter = 1

        if self.data[0] == -1 and other.data[0] == 1:
            output2 = other + self
            output = output2.data

        elif self.data[0] == -1 and other.data[0] == -1:
            self.data[0] = 1
            other.data[0] = 1
            output2 = self + other
            output2.data[0] = -1
            output = output2.data

        else: 
            output.insert(0,1)

            while len(self.data) > len(other.data):
                other.data.insert(1, 0)

            while len(other.data) > len(self.data):
                self.data.insert(1, 0)
                    
            while ((len(self.data)-1) - whileCounter) >= 0: 
                            
                if self.data[0] == 1 and other.data[0] == -1:
                    other.data[0] = 1
                    if self < other:
                        self.data[0] = -1
                        output2 = other + self
                        output2.data[0] = -1
                        output = output2.data
                        break
                    other.data[0] = -1

                    digit = self.data[len(self.data)-whileCounter] - other.data[len(other.data)-whileCounter] - carryOnNum
                    if digit < 0:
                        carryOnNum = 1
                        output.insert(1, digit+10)
                    else:    
                        carryOnNum = 0
                        if ((len(self.data)-1) - whileCounter) == 0 and self.data[1] == other.data[1]:
                            if len(self.data) == 2:
                                output.insert(1, 0)
                            break
                        else:
                            output.insert(1, digit)
                    whileCounter = whileCounter + 1        

                else:
                    digit = self.data[len(self.data)-whileCounter] + other.data[len(other.data)-whileCounter] + carryOnNum
                    if digit > (self.packLength-1):
                        carryOnNum = int((digit - digit % 10)/10)
                        digit = digit % 10
                        output.insert(1, digit)
                    else:
                        output.insert(1, digit)
                        carryOnNum = 0

                    whileCounter = whileCounter + 1
                    if carryOnNum > 0 and len(self.data)-whileCounter == 0:
                        output.insert(1,carryOnNum)

        if output == [-1,0]:
            output[0] = 1

        elif output == [1]:
            output.append(0)

        if type(output) != BigNumber:
            if len(output) > 2:
                while output[1] == 0 and len(output) > 2:
                    output.pop(1)

        newObject.data = output
        return newObject

    def __cmp(self, other):
        
        if self.data[0] > other.data[0]:
            output = 1
        elif self.data[0] < other.data[0]:
            output = -1
        else:
            if len(self.data) > len(other.data):
                if self.data[0] == 1:
                    output = 1
                else:
                    output = -1
            elif len(self.data) < len(other.data):
                if self.data[0] == 1:
                    output = -1
                else:
                    output = 1
            else:
                
                different = False
                output = 0
                whileCounter = 1

                while different == False:

                    if self.data[whileCounter] > other.data[whileCounter]:
                        different = True
                        if self.data[0] == -1 and other.data[0] == -1:
                            output = -1
                        else:    
                            output = 1
                    elif self.data[whileCounter] < other.data[whileCounter]:
                        different = True
                        if self.data[0] == -1 and other.data[0] == -1:
                            output = 1
                        else:    
                            output = -1
                    else:
                        whileCounter = whileCounter + 1
                        if whileCounter > len(self.data)-1 or whileCounter > len(other.data)-1:
                            output = 0 
                            break

        return(output)
    
    def __mul(x, y):
        
        carryOnNum = 0
        whileCounter1 = 1
        whileCounter2 = 1    
        output = BigNumber(0)
        mullAdd = BigNumber([1])

        if len(x) == 2 and len(y) > len(x):
            output.data = BigNumber.__mul(y,x)

        elif y[len(y)-1] == 0:
            y.pop()
            output.data = BigNumber.__mul(x,y)
            output.data.append(0)
        
        else:

            while ((len(y)-1) - whileCounter1) >= 0:

                while ((len(x)-1) - whileCounter2) >= 0:
                    digit = y[1] * x[len(x)-whileCounter2] + carryOnNum
                    carryOnNum = int(digit / BigNumber.packLength)
                    mullAdd.data.insert(1,digit % BigNumber.packLength)
                    whileCounter2 = whileCounter2 + 1
                
                output = output + mullAdd

                while len(output.data) < len(mullAdd.data):
                    output.data.insert(1,0)

                #if ((len(y)-1) - whileCounter1) != 0:
                #    output.append(0)

                if ((len(y)-1) - whileCounter1) <= 0:
                    output.data.insert(1,carryOnNum)
                    break
                
                whileCounter1 = whileCounter1 + 1

            if x[0] != y[0]:
                output.data[0] = -1
        
        if len(output.data) > 2:
            while output.data[1] == 0 and len(output.data) > 2:
                output.data.pop(1)

        return(output.data)
    
    def __gt__(self, other):

        if self.__cmp(other) == 1:
            return True
        
        return False
    
    def __eq__(self, other):

        if self.__cmp(other) == 0:
            return True
        
        return False
    
    def __sub__(self,other):

        newObject = BigNumber(0)

        other.data[0] = other.data[0]*(-1)
        newObject = self + other
        other.data[0] = other.data[0]*(-1)
        return(newObject)

    def __mul__(self, other):
        
        newNumber = BigNumber(0)
        newNumber.data = BigNumber.__mul(self.data,other.data)
        return newNumber

    def __floordiv__(self,other):

        lenSelfData = len(self.data) - 1
        
        if other.data != [1,10] and other.data != [1,100]:
            assert False , "Not yet Avalible"

        for i in range(lenSelfData):
            self.data[lenSelfData-i] = self.data[lenSelfData] // other.data[1]
            if lenSelfData != 1:
                self.data[lenSelfData-i] += (self.data[lenSelfData-i-1] % 10)*(self.packLength / 10)

        if self.data == [1]:
            self.data.insert(1,0)

        return self
    
    def __int__(self):
        output = 0

        for i in self.data[1:]:
            output = output * 10000+i

        return output*self.data[0]

#def stringCnv(x):
#    whileCounter = 1
#    output = ""
#    if x[0] == -1:
#            x.pop(0)
#            output = output + "-"
#    else:
#        x.pop(0)
#
#    while len(x) - whileCounter >= 0:
#        output = output + str(x[whileCounter-1])
#        whileCounter = whileCounter +1
#
#    return(output)

def arrayToInt(x):

    output = 0

    for i in x[1:]:
        output = output*10+i

    return output*x[0]
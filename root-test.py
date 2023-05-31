from root import *
from root2reference import *
import time
import matplotlib.pyplot as plt    # call 'pip install matplotlib'



#############################################################
#
# test results of root()
#
#############################################################

def rootTest(a, decimalPlaces):
    print("Calculate root of " + str(a) + " with " + str(decimalPlaces) + " decimal places")
    x = root(a,decimalPlaces)
    assert rootOf2.startswith(x) == True,x
    
x = rootTest(2,0)
x = rootTest(2,1)
x = rootTest(2,50)
x = rootTest(2,100)
x = rootTest(2,150)
x = rootTest(2,200)
x = rootTest(2,250)
x = rootTest(2,300)
x = rootTest(2,1000)
x = rootTest(2,5000)

#############################################################
#
# test timing of root()
#
#############################################################

chartDecimals = []
chartSecs = []

def timeTest(decimals, iterations=10):
    tStart = time.time()

    for i in range(iterations):
        x = root(2,decimals)
    
    tEnd = time.time()
    tCalc = (tEnd-tStart)/iterations*1000
    chartSecs.append(tCalc)
    chartDecimals.append(decimals)

    assert rootOf2.startswith(x) == True,x

    print(str(decimals) + " decimal places: " + str(int(tCalc)/1000) + " s")


timeTest(0)
timeTest(50)
timeTest(100)
timeTest(150)
timeTest(200)
timeTest(250)
timeTest(300)
timeTest(600)
timeTest(1200)
timeTest(2000)
timeTest(3000)
timeTest(4200)

plt.plot(chartDecimals,chartSecs)
plt.show()

#############################################################
#
# test results of splitNumber()
#
#############################################################

x = splitNumber(0);                         assert x == [0],x
x = splitNumber(1);                         assert x == [1],x
x = splitNumber(12);                        assert x == [12],x
x = splitNumber(123);                       assert x == [1,23],x
x = splitNumber(1234);                      assert x == [12,34],x
x = splitNumber(12345);                     assert x == [1,23,45],x
x = splitNumber(123456);                    assert x == [12,34,56],x
x = splitNumber(1234567);                   assert x == [1,23,45,67],x

#############################################################
#
# test results of rootOfFirstItem()
#
#############################################################

x = rootOfFirstItem(84);                    assert x == 9,x
x = rootOfFirstItem(35);                    assert x == 5,x
x = rootOfFirstItem(48);                    assert x == 6,x
x = rootOfFirstItem(10);                    assert x == 3,x

#############################################################
#
# test results of rootDigitCalculator()
#
#############################################################

x = rootDigitCalculator(800,8);             assert x == 4,x
x = rootDigitCalculator(700,8);             assert x == 4,x
x = rootDigitCalculator(600,8);             assert x == 3,x

assert 1==0, "all Tests passed"
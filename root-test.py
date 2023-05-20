from root import *
import time

#############################################################
#
# test results of root()
#
#############################################################

rootOf2 = "1,414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572735013846230912297024924836055850737212644121497099935831413222665927505592755799950501152782060571470109559971605970274534596862014728517418640889198609552329230484308714321450839762603627995251407989687253396546331808829640620615258352395054745750287759961729835575220337531857011354374603408498847160386899970699004815030544027790316454247823068492936918"

x = root(2,0);                              assert rootOf2.startswith(x) == True,x
x = root(2,1);                              assert rootOf2.startswith(x) == True,x
x = root(2,50);                             assert rootOf2.startswith(x) == True,x
x = root(2,100);                            assert rootOf2.startswith(x) == True,x
x = root(2,150);                            assert rootOf2.startswith(x) == True,x
x = root(2,200);                            assert rootOf2.startswith(x) == True,x
x = root(2,250);                            assert rootOf2.startswith(x) == True,x
x = root(2,300);                            assert rootOf2.startswith(x) == True,x
x = root(2,307);                            assert rootOf2.startswith(x) == True,x

#############################################################
#
# test timing of root()
#
#############################################################

def timeTest(decimals, iterations=100):
    tStart = time.time()

    for i in range(iterations):
        x = root(2,decimals)

    tEnd = time.time()
    print(str(decimals) + " decimal places: " + str((tEnd-tStart)/iterations*1000) + " ms")

timeTest(0)
timeTest(50)
timeTest(100)
timeTest(150)
timeTest(200)
timeTest(250)
timeTest(300)

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
from bignumber import *
import time

#############################################################
#
# test results of cnv()
#
#############################################################

x = BigNumber(1234567);                     assert x.data == [1,1,234567],      x.data
x = BigNumber(-1234567);                    assert x.data == [-1,1,234567],     x.data
x = BigNumber(0);                           assert x.data == [1,0],             x.data
x = BigNumber(20);                          assert x.data == [1,20],            x.data

#############################################################
#
# test results of cmp()
#
#############################################################

x = BigNumber(0) == BigNumber(0);           assert x == True


x = BigNumber(-0) == BigNumber(-0);         assert x == True
x = BigNumber(123456) == BigNumber(123456); assert x == True
x = BigNumber(1) == BigNumber(1);           assert x == True
x = BigNumber(234512) == BigNumber(234512); assert x == True
x = BigNumber(83525283) == BigNumber(83525283);      assert x == True

x = BigNumber(5) > BigNumber(0);            assert x == True
x = BigNumber(999) > BigNumber(234);        assert x == True
x = BigNumber(123456) > BigNumber(234);     assert x == True
x = BigNumber(123) > BigNumber(-123);       assert x == True
x = BigNumber(124) > BigNumber(-123);       assert x == True
x = BigNumber(123) > BigNumber(-124);       assert x == True
x = BigNumber(-234) > BigNumber(-456);      assert x == True
x = BigNumber(-5) > BigNumber(-6);          assert x == True

x = BigNumber(0) < BigNumber(5);            assert x == True
x = BigNumber(234) < BigNumber(999);        assert x == True
x = BigNumber(234) < BigNumber(123456);     assert x == True 
x = BigNumber(-123) < BigNumber(123);       assert x == True
x = BigNumber(-123) < BigNumber(124);       assert x == True
x = BigNumber(-124) < BigNumber(123);       assert x == True
x = BigNumber(-456) < BigNumber(-234);      assert x == True
x = BigNumber(-6) < BigNumber(-5);          assert x == True

a = [8] * 1000000
b = [8] * 1000000
a[0] = 1
b[0] = 1
x = a == b;                                 assert x == True

a[999] = 0
b[999] = 1
x = a < b;                                  assert x == True

a[999] = 1
b[999] = 0
x = a > b;                                  assert x == True

a = [1,2,3]*1000
b = [1,2,4]*1000
x = a < b;                                  assert x == True

#############################################################
#
# test timing of cmp()
#
#############################################################

def timeCmp(x, y):
    a = BigNumber(x)
    b = BigNumber(y)

    tStart = time.time()
    c = a > b
    tEnd = time.time()
    print("Comparing " + str(len(x)-1) + " digits with " + str(len(y)-1) + " digits in: " + str(tEnd-tStart) + " sec")

timeCmp([1]*1000001,[1]*1000001)
timeCmp([1]*1001,[1]*11)
#timeCmp([1]*self.packLength1,[1]*self.packLength1) # 100mio --> takes forever
timeCmp([1,2,3]*100000,[1,2,4]*1000000)

#############################################################
#
# test results of add()
#
#############################################################

x = BigNumber(1) + BigNumber(1);            assert x.data == [1,2],             x.data
x = BigNumber(-9) + BigNumber(9);           assert x.data == [1,0],             x.data
x = BigNumber(12) + BigNumber(29);          assert x.data == [1,41],           x.data
x = BigNumber(123) + BigNumber(294);        assert x.data == [1,417],         x.data

x = BigNumber(-1) + BigNumber(1);           assert x.data == [1,0],             x.data
x = BigNumber(-9) + BigNumber(-9);          assert x.data == [-1,18],          x.data
x = BigNumber(-12) + BigNumber(29);         assert x.data == [1,17],           x.data
x = BigNumber(123) + BigNumber(48);         assert x.data == [1,171],         x.data

#############################################################
#
# test results of sub()
#
#############################################################

x = BigNumber(2) - BigNumber(9);            assert x.data == [-1,7],            x.data
x = BigNumber(3) - BigNumber(92);           assert x.data == [-1,89],          x.data
x = BigNumber(4) - BigNumber(915);          assert x.data == [-1,911],        x.data   
x = BigNumber(5) - BigNumber(9269);         assert x.data == [-1,9264],      x.data

x = BigNumber(2) - BigNumber(-9);           assert x.data == [1,11],           x.data
x = BigNumber(3) - BigNumber(-92);          assert x.data == [1,95],           x.data
x = BigNumber(4) - BigNumber(-915);         assert x.data == [1,919],         x.data   
x = BigNumber(5) - BigNumber(-9269);        assert x.data == [1,9274],       x.data

x = BigNumber(-2) - BigNumber(9);           assert x.data == [-1,11],          x.data
x = BigNumber(-3) - BigNumber(92);          assert x.data == [-1,95],          x.data
x = BigNumber(-4) - BigNumber(915);         assert x.data == [-1,919],        x.data   
x = BigNumber(-5) - BigNumber(9269);        assert x.data == [-1,9274],      x.data

x = BigNumber(-2) - BigNumber(-9);          assert x.data == [1,7],             x.data
x = BigNumber(-3) - BigNumber(-92);         assert x.data == [1,89],           x.data
x = BigNumber(-4) - BigNumber(-915);        assert x.data == [1,911],         x.data
x = BigNumber(-5) - BigNumber(-9269);       assert x.data == [1,9264],       x.data

x = BigNumber(9) - BigNumber(2);            assert x.data == [1,7],             x.data
x = BigNumber(92) - BigNumber(3);           assert x.data == [1,89],           x.data
x = BigNumber(915) - BigNumber(4);          assert x.data == [1,911],         x.data
x = BigNumber(9296) - BigNumber(5);         assert x.data == [1,9291],       x.data

x = BigNumber(-9) - BigNumber(2);           assert x.data == [-1,11],          x.data
x = BigNumber(-92) - BigNumber(3);          assert x.data == [-1,95],          x.data
x = BigNumber(-915) - BigNumber(4);         assert x.data == [-1,919],        x.data
x = BigNumber(-9296) - BigNumber(5);        assert x.data == [-1,9301],      x.data

#############################################################
#
# test results of mul()
#
#############################################################

x = BigNumber(2) * BigNumber(9);            assert x.data == [1,18],           x.data
x = BigNumber(3) * BigNumber(92);           assert x.data == [1,276],         x.data
x = BigNumber(4) * BigNumber(915);          assert x.data == [1,3660],       x.data   
x = BigNumber(5) * BigNumber(9269);         assert x.data == [1,46345],     x.data

x = BigNumber(2) * BigNumber(-9);           assert x.data == [-1,18],          x.data
x = BigNumber(3) * BigNumber(-92);          assert x.data == [-1,276],        x.data
x = BigNumber(4) * BigNumber(-915);         assert x.data == [-1,3660],      x.data   
x = BigNumber(5) * BigNumber(-9269);        assert x.data == [-1,46345],    x.data

x = BigNumber(-2) * BigNumber(9);           assert x.data == [-1,18],          x.data
x = BigNumber(-3) * BigNumber(92);          assert x.data == [-1,276],        x.data
x = BigNumber(-4) * BigNumber(915);         assert x.data == [-1,3660],      x.data   
x = BigNumber(-5) * BigNumber(9269);        assert x.data == [-1,46345],    x.data

x = BigNumber(-2) * BigNumber(-9);          assert x.data == [1,18],           x.data
x = BigNumber(-3) * BigNumber(-92);         assert x.data == [1,276],         x.data
x = BigNumber(-4) * BigNumber(-915);        assert x.data == [1,3660],       x.data   
x = BigNumber(-5) * BigNumber(-9269);       assert x.data == [1,46345],     x.data

x = BigNumber(9) * BigNumber(2);            assert x.data == [1,18],           x.data
x = BigNumber(92) * BigNumber(3);           assert x.data == [1,276],         x.data
x = BigNumber(915) * BigNumber(4);          assert x.data == [1,3660],       x.data   
x = BigNumber(9269) * BigNumber(5);         assert x.data == [1,46345],     x.data

x = BigNumber(-9) * BigNumber(2);           assert x.data == [-1,18],          x.data
x = BigNumber(-92) * BigNumber(3);          assert x.data == [-1,276],        x.data
x = BigNumber(-915) * BigNumber(4);         assert x.data == [-1,3660],      x.data   
x = BigNumber(-9269) * BigNumber(5);        assert x.data == [-1,46345],    x.data

x = BigNumber(1) * BigNumber(20);           assert x.data == [1,20],           x.data
x = BigNumber(20) * BigNumber(5);           assert x.data == [1,100],         x.data
x = BigNumber(1) * BigNumber(20) * BigNumber(5);   assert x.data == [1,100],  x.data
x = BigNumber(123) * BigNumber(1);          assert x.data == [1,123],         x.data
x = BigNumber(1414) * BigNumber(20);        assert x.data == [1,28280],     x.data

#############################################################
#
# test results of div()
#
#############################################################

x = BigNumber(2345) // BigNumber(10);        assert x.data == [1,234],        x.data
x = BigNumber(2345) // BigNumber(100);       assert x.data == [1,23],          x.data
x = BigNumber(0) // BigNumber(10);           assert x.data == [1,0],            x.data
x = BigNumber(10) // BigNumber(10);          assert x.data == [1,1],            x.data
x = BigNumber(10) // BigNumber(100);         assert x.data == [1,0],            x.data
x = BigNumber(100) // BigNumber(100);        assert x.data == [1,1],            x.data
x = BigNumber(100) // BigNumber(10);         assert x.data == [1,10],          x.data
x = BigNumber(-123) // BigNumber(10);        assert x.data == [-1,12],         x.data

#############################################################
#
# test results of cnvString()
#
#############################################################

#x = stringCnv([1,1,2,3,4,5]);               assert x == "12345",x
#x = stringCnv([-1,1,2,3,4,5,6]);            assert x == "-123456",x
#x = stringCnv([1,0]);                       assert x == "0",x

#############################################################
#
# test results of arrayToInt()
#
#############################################################

x = int(BigNumber([1,1234567]));       assert x == 1234567
x = int(BigNumber([-1,1234567]));      assert x == -1234567
x = int(BigNumber([1,0]));                   assert x == 0
x = int(BigNumber([1,1000]));             assert x == 1000

assert 1==0, "all Tests passed"
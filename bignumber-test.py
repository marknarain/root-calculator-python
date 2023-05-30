from bignumber import *
import time

#############################################################
#
# test results of cnv()
#
#############################################################

x = BigNumber(1234567);                     assert x.data == [1,1,2,3,4,5,6,7],x
x = BigNumber(-1234567);                    assert x.data == [-1,1,2,3,4,5,6,7],x
x = BigNumber(0);                           assert x.data == [1,0],x
x = BigNumber(20);                          assert x.data == [1,2,0],x

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

tStart = time.time()
x = cmp([1]*1000001,[1]*1000001)
tEnd = time.time()
print("Comparing 1mio digits: " + str(tEnd-tStart) + " sec")

tStart = time.time()
x = cmp([1]*1001,[1]*11)
tEnd = time.time()
print("Comparing 1000 with 10 digits: " + str(tEnd-tStart) + " sec")

#tStart = time.time()
#x = cmp([1]*100000001,[1]*100000001)
#tEnd = time.time()
#print("Comparing 100mio digits: " + str(tEnd-tStart) + " sec")

tStart = time.time()
x = cmp([1,2,3]*100000,[1,2,4]*1000000)
tEnd = time.time()
print("Comparing 3000 digits: " + str(tEnd-tStart) + " sec")

#############################################################
#
# test results of add()
#
#############################################################

x = BigNumber(1) + BigNumber(1);            assert x.data == [1,2],x
x = BigNumber(-9) + BigNumber(9);           assert x.data == [1,0],x
x = BigNumber(12) + BigNumber(29);          assert x.data == [1,4,1],x
x = BigNumber(123) + BigNumber(294);        assert x.data == [1,4,1,7],x

x = BigNumber(-1) + BigNumber(1);           assert x.data == [1,0],x
x = BigNumber(-9) + BigNumber(-9);          assert x.data == [-1,1,8],x
x = BigNumber(-12) + BigNumber(29);         assert x.data == [1,1,7],x
x = BigNumber(123) + BigNumber(294);        assert x.data == [1,1,7,1],x

#############################################################
#
# test results of sub()
#
#############################################################

x = sub([1,2],[1,9]);                       assert x == [-1,7],x
x = sub([1,3],[1,9,2]);                     assert x == [-1,8,9],x
x = sub([1,4],[1,9,1,5]);                   assert x == [-1,9,1,1],x   
x = sub([1,5],[1,9,2,6,9]);                 assert x == [-1,9,2,6,4],x

x = sub([1,2],[-1,9]);                      assert x == [1,1,1],x
x = sub([1,3],[-1,9,2]);                    assert x == [1,9,5],x
x = sub([1,4],[-1,9,1,5]);                  assert x == [1,9,1,9],x   
x = sub([1,5],[-1,9,2,6,9]);                assert x == [1,9,2,7,4],x

x = sub([-1,2],[1,9]);                      assert x == [-1,1,1],x
x = sub([-1,3],[1,9,2]);                    assert x == [-1,9,5],x
x = sub([-1,4],[1,9,1,5]);                  assert x == [-1,9,1,9],x   
x = sub([-1,5],[1,9,2,6,9]);                assert x == [-1,9,2,7,4],x

x = sub([-1,2],[-1,9]);                     assert x == [1,7],x
x = sub([-1,3],[-1,9,2]);                   assert x == [1,8,9],x
x = sub([-1,4],[-1,9,1,5]);                 assert x == [1,9,1,1],x   
x = sub([-1,5],[-1,9,2,6,9]);               assert x == [1,9,2,6,4],x

x = sub([1,9],[1,2]);                       assert x == [1,7],x
x = sub([1,9,2],[1,3]);                     assert x == [1,8,9],x
x = sub([1,9,1,5],[1,4]);                   assert x == [1,9,1,1],x   
x = sub([1,9,2,6,9],[1,5]);                 assert x == [1,9,2,6,4],x

x = sub([1,9],[-1,2]);                      assert x == [1,1,1],x
x = sub([1,9,2],[-1,3]);                    assert x == [1,9,5],x
x = sub([1,9,1,5],[-1,4]);                  assert x == [1,9,1,9],x   
x = sub([1,9,2,6,9],[-1,5]);                assert x == [1,9,2,7,4],x

a = [1,1,2,3]
b = [-1,2,3,4]
x = sub(a,b)
print(a,b)

#############################################################
#
# test results of mul()
#
#############################################################

x = mul([1,2],[1,9]);                       assert x == [1,1,8],x
x = mul([1,3],[1,9,2]);                     assert x == [1,2,7,6],x
x = mul([1,4],[1,9,1,5]);                   assert x == [1,3,6,6,0],x   
x = mul([1,5],[1,9,2,6,9]);                 assert x == [1,4,6,3,4,5],x

x = mul([1,2],[-1,9]);                      assert x == [-1,1,8],x
x = mul([1,3],[-1,9,2]);                    assert x == [-1,2,7,6],x
x = mul([1,4],[-1,9,1,5]);                  assert x == [-1,3,6,6,0],x   
x = mul([1,5],[-1,9,2,6,9]);                assert x == [-1,4,6,3,4,5],x

x = mul([-1,2],[1,9]);                      assert x == [-1,1,8],x
x = mul([-1,3],[1,9,2]);                    assert x == [-1,2,7,6],x
x = mul([-1,4],[1,9,1,5]);                  assert x == [-1,3,6,6,0],x  
x = mul([-1,5],[1,9,2,6,9]);                assert x == [-1,4,6,3,4,5],x

x = mul([-1,2],[-1,9]);                     assert x == [1,1,8],x
x = mul([-1,3],[-1,9,2]);                   assert x == [1,2,7,6],x
x = mul([-1,4],[-1,9,1,5]);                 assert x == [1,3,6,6,0],x 
x = mul([-1,5],[-1,9,2,6,9]);               assert x == [1,4,6,3,4,5],x

x = mul([1,9],[1,2]);                       assert x == [1,1,8],x
x = mul([1,9,2],[1,3]);                     assert x == [1,2,7,6],x
x = mul([1,9,1,5],[1,4]);                   assert x == [1,3,6,6,0],x   
x = mul([1,9,2,6,9],[1,5]);                 assert x == [1,4,6,3,4,5],x

x = mul([1,9],[-1,2]);                      assert x == [-1,1,8],x
x = mul([1,9,2],[-1,3]);                    assert x == [-1,2,7,6],x
x = mul([1,9,1,5],[-1,4]);                  assert x == [-1,3,6,6,0],x 
x = mul([1,9,2,6,9],[-1,5]);                assert x == [-1,4,6,3,4,5],x

x = mul([1,1],[1,2,0]);                     assert x == [1,2,0],x
x = mul([1,2,0],[1,5]);                     assert x == [1,1,0,0],x
x = mul(mul([1,1],[1,2,0]),[1,5]);          assert x == [1,1,0,0],x
x = mul([1,1,2,3],[1,1]);                   assert x == [1,1,2,3],x
x = mul([1,1,4,1,4],[1,2,0]);               assert x == [1,2,8,2,8,0],x

#############################################################
#
# test results of div()
#
#############################################################

x = div([1,2,3,4,5],[1,1,0]);               assert x == [1,2,3,4],x
x = div([1,2,3,4,5],[1,1,0,0]);             assert x == [1,2,3],x
x = div([1,0],[1,1,0]);                     assert x == [1,0],x
x = div([1,1,0],[1,1,0]);                   assert x == [1,1],x
x = div([1,1,0],[1,1,0,0]);                 assert x == [1,0],x
x = div([1,1,0,0],[1,1,0,0]);               assert x == [1,1],x
x = div([1,1,0,0],[1,1,0]);                 assert x == [1,1,0],x
x = div([-1,1,2,3],[1,1,0]);                assert x == [-1,1,2],x

#############################################################
#
# test results of cnvString()
#
#############################################################

x = stringCnv([1,1,2,3,4,5]);               assert x == "12345",x
x = stringCnv([-1,1,2,3,4,5,6]);            assert x == "-123456",x
x = stringCnv([1,0]);                       assert x == "0",x

#############################################################
#
# test results of arrayToInt()
#
#############################################################

x = arrayToInt([1,1,2,3,4,5,6,7]);          assert x == 1234567
x = arrayToInt([-1,1,2,3,4,5,6,7]);         assert x == -1234567
x = arrayToInt([1,0]);                      assert x == 0
x = arrayToInt([1,1,0,0,0]);                assert x == 1000

assert 1==0, "all Tests passed"
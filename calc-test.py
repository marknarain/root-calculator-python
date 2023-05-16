from calc import *
import time

#############################################################
#
# test results of cmp()
#
#############################################################
x = cmp([1,0],[1,0]);                     assert x == 0,x
x = cmp([-1,0],[-1,0]);                   assert x == 0,x
x = cmp([1,1,2,3,4,5,6],[1,1,2,3,4,5,6]); assert x == 0,x

x = cmp([1,5],[1,0]);                      assert x == 1,x
x = cmp([1,9,9,9],[1,2,3,4]);              assert x == 1,x
x = cmp([1,1,2,3,4,5,6],[1,2,3,4]);        assert x == 1,x
x = cmp([1,1,2,3],[-1,1,2,3]);             assert x == 1,x
x = cmp([1,1,2,4],[-1,1,2,3]);             assert x == 1,x
x = cmp([1,1,2,3],[-1,1,2,4]);             assert x == 1,x

x = cmp([1,0],[1,5]);                      assert x == -1,x
x = cmp([1,1,2,3],[1,2,3,4]);              assert x == -1,x
x = cmp([1,2,3,4],[1,1,2,3,4,5,6]);        assert x == -1,x   
x = cmp([-1,1,2,3],[1,1,2,3]);             assert x == -1,x
x = cmp([-1,1,2,4],[1,1,2,3]);             assert x == -1,x
x = cmp([-1,1,2,3],[1,1,2,4]);             assert x == -1,x

a = [8] * 1000000
b = [8] * 1000000
a[0] = 1
b[0] = 1
x = cmp(a,b);  assert x == 0,x

a[999] = 0
b[999] = 1
x = cmp(a,b);  assert x == -1,x
a[999] = 1
b[999] = 0
x = cmp(a,b);  assert x == 1,x

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


assert 1==0, "all Tests passed"
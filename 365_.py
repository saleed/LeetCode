import queue

###超时
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        visState=set()
        visState.add(complex(0,0))
        que=queue.Queue()
        que.put(complex(0,0))
        while not que.empty():

            tmp=que.get()
            # print tmp
            if tmp.real==z or tmp.imag==z or tmp.real+tmp.imag==z:
                return True
            #pure x
            if complex(0,tmp.imag) not in visState:
                visState.add(complex(0,tmp.imag))
                que.put(complex(0,tmp.imag))
            if complex(tmp.real,0) not in visState:
                visState.add(complex(tmp.real,0))
                que.put(complex(tmp.real,0))
            #fill x
            if complex(x,tmp.imag) not in visState:
                visState.add(complex(x,tmp.imag))
                que.put(complex(x,tmp.imag))
            #fill y
            if complex(tmp.real,y) not in visState:
                que.put(complex(tmp.real,y))
                visState.add(complex(tmp.real,y))

            #pure x into y
            if tmp.real+tmp.imag<=y and  complex(0,tmp.real+tmp.imag) not in visState:
                que.put(complex(0,tmp.real+tmp.imag))
                visState.add(complex(0,tmp.real+tmp.imag))
            if tmp.real+tmp.imag>y and complex(tmp.real+tmp.imag-y,y) not in visState:
                que.put(complex(tmp.real+tmp.imag-y,y))
                visState.add(complex(tmp.real+tmp.imag-y,y))
            #pure y into x
            if tmp.real+tmp.imag<=x and  complex(tmp.real+tmp.imag,0) not in visState:
                que.put(complex(tmp.real+tmp.imag,0))
                visState.add(complex(tmp.real+tmp.imag,0))
            if tmp.real+tmp.imag>x and complex(x,tmp.real+tmp.imag-x) not in visState:
                que.put(complex(x,tmp.real+tmp.imag-x))
                visState.add(complex(x,tmp.real+tmp.imag-x))
        return False

x = 3
y = 5
z = 4
a=Solution()
print(a.canMeasureWater(x,y,z))


d=complex(1,2)
print(d.real)
f=set()
f.add(1)
f.add(complex(1,1))
print(complex(1,1) not in f)


x=104639
y=104651
z=234
print(a.canMeasureWater(x,y,z))



# 找到x,y的最大公约数能否z被整除

class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if x+y < z:
            return False
        if x>y:
            x,y=y,x
        if x == 0:
            return y==z
        while y%x != 0:
            y,x = x,y%x
        return z%x==0
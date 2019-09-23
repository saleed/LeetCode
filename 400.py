class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<10:
            return n
        bitnum=2
        cur=9
        while 9*(10**(bitnum-1))+cur<n:
            bitnum+=1
            cur+=9*(10**(bitnum-1))
        res=10**(bitnum-1)+(n-cur-1)/bitnum
        print res
        left=(n-cur-1)%bitnum
        rrr=-1
        while bitnum-left>0:
            rrr=res%10
            res/=10
            left+=1
        return rrr
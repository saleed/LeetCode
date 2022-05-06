class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        sumnum=0
        while sumnum<n:
            sumnum+=9*pow(10,i-1)*i
            i+=1
        i-=1
        sumnum-=9*pow(10,i-1)*i
        left=n-sumnum-1

        digit=left/i+pow(10,i-1)
        c=left%i
        return int(str(digit)[c])






    def fac(self,n):
        res=1
        for i in range(n+1):
            res*=i
        return res









    def fac(self,n):
        res=1
        for i in range(n+1):
            res*=i
        return res

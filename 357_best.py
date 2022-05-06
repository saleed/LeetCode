class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n>=10:
            return
        dp=[0]*n

        dp[0]=10
        r=n
        for i in range(1,n):
            dp[i]=dp[i-1]+9*self.fac(9)/self.fac(9-(n-1))
        return dp[-1]




    def fac(self,n):
        res=1
        for i in range(n+1):
            res*=i
        return res
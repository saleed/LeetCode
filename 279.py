import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[float("inf")]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n+1):
            j=1
            while i>=j*j:
                dp[i]=min(dp[i],dp[i-j*j]+1)
                j+=1
        # print dp
        return dp[n]



t=5
print math.sqrt(t)  
print int(math.sqrt(t))==int(t)
p=4
print int(math.sqrt(p))==math.sqrt(p)

a=Solution()
print a.numSquares(12)
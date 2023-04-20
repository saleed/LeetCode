class Solution(object):
    def maxA(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp=[float("inf")]*(n+1)
        dp[0]=0
        dp[1]=1
        for i in range(2,n):
            dp[i]=dp[i-1]+1
            if i-3>0:
                dp[i]=max(dp[i],dp[i-3]*2)
        return dp[-1]




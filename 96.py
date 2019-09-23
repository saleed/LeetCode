class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0 for _ in range(n+1)]
        for i in range(1,n+1):
            dp[i]=0
            for j in range(i):
                dp[i]+=dp[j]*dp[i-j-1]
        return dp[n]



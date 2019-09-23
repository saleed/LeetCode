class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(1,n+1):
            for j in range(1,i):
                dp[i]=max(dp[i],max(dp[j],j)*(i-j))  ###be careful for this

        return dp[n]
a=Solution()
print(a.integerBreak(2))
print(a.integerBreak(10))

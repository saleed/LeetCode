class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp=[n]*(n+1)
        if n==1:
            return 0
        dp[1]=0
        for i in range(2,n+1):
            for j in range(1,i)[::-1]:
                if i%j==0:
                    dp[i]=dp[j]+i/j  ##找到一个最大的可以整除的 ##其实是 dp[i]=dp[j]+i/j-1+1
                    break
        return dp[-1]


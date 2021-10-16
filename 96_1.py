class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp=[0]*(n+1)  ##这里的n是长度
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(i): ##这里的j对应长度为i的数组的下标
                dp[i]+=dp[j]*dp[i-1-j]
        print(dp)
        return dp[-1]


a=Solution()
print(a.numTrees(3))
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp=[[1 for _ in range(n)] for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         dp[i][j]+=dp[i-1][j] if i>0 else 0
        #         dp[i][j]+=dp[i][j-1] if j>0 else 0
        # return dp[-1][-1]


        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]
        return dp[n - 1]

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        dp = [[float("inf") if i <= j else 0 for j in range(n + 2)] for i in range(n + 2)]

        for intv in range(n + 1):
            for i in range(1, n + 1):
                if intv == 0:
                    dp[i][i + intv] = 0
                    continue
                if i + intv < n + 1:
                    for j in range(i, i + intv + 1):
                        # print(i,i+intv,j,dp[i][i+intv],dp[i][j-1],dp[j+1][i+intv])

                        dp[i][i + intv] = min(dp[i][i + intv], j + max(dp[i][j - 1], dp[j + 1][i + intv]))

        # for i in range(n+1):
        #     print(dp[i])
        return dp[1][n]

class Solution(object):


    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        dp = [[0 for _ in range(2)] for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = k
        for i in range(1, n):
            dp[i][0] = dp[i - 1][1]
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) * (k - 1)
        return sum(dp[n - 1])
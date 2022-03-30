class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[float("inf") for _ in range(amount+1)]
        dp[0]=0
        for i in range(amount+1):
            for c in coins:
                if i-j>=0:
                    dp[i]=min(dp[i],dp[i-c]+1)
        return dp[-1]
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return 0
        dp=[float("inf")]*(amount+1)
        for i in coins:
            if i<=amount:
                dp[i]=1
        for i in range(amount+1):
            for j in coins:
                if i-j>=0:
                    dp[i]=min(dp[i],1+dp[i-j])
        return dp[amount] if dp[amount]!=float("inf") else -1

a=Solution()
coins = [1, 2, 5]
amount = 11
print(a.coinChange(coins,amount))

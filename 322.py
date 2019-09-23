class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #greedy mthod is wrong solution, like tsp this can be soloved by dp
        #dp[n][amount],n is the coin index

        #at first  i want to use dfs.but thought too compicated and without use the Memorized Search,
        dp=[0]+[float("inf")]*amount
        for i in range(1,amount+1):
            dp[i]=min(dp[i-c] if i-c>=0 else float("inf") for c in coins)+1

        return dp[amount] if dp[amount]!=float("inf") else -1


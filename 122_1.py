class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.dp(prices)



    def greedy(self,prices):
        maxbenefit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                maxbenefit+=prices[i]-prices[i-1]
        return maxbenefit


    ##还有一种方法是动态规划


    def  dp(self,price):
        dp=[[0 for _ in range(2)] for _ in range(len(price))]

        ####定义dp[i][0]表示未持有的时候的最大收益
        ####定义dp[i][1]表示持有的时候的最大收益
        dp[0][0]=0
        dp[0][1]=-price[0]

        for i in range(1,len(price)):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+price[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-price[i])
        return dp[-1][0]

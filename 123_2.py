class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices)==0:
            return 0


        dp=[[[ i for i in range(2)] for _ in range(k)] for _ in range(len(prices))]

        dp[i][k][0]=max(dp[i-1][k][0],dp[i-1][k-1][1]+prices[i])
        dp[i][k][1]=max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])


        dp[i][0][0]=dp[i][0][1]=0



        for i in range(len(prices)):
            for k in range(k):





prices=[3,3,5,0,0,3,1,4]
a=Solution()


# prices=[1,2,3,4,5]
print(a.maxProfit(prices))

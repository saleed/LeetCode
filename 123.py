class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        dp=[[[ i for i in range(2)] for _ in range(k)] for _ in range(len(prices))]

        dp[i][k][0]=max(dp[i-1][k][0],dp[i-1][k-1][1]+prices[i])
        dp[i][k][1]=max(dp[i-1][k][1],dp[i-1][k-1][0]-prices[i])


        dp[i][0][0]=dp[i][0][1]=0
        if len(prices)==0:
            return 0


        maxProfitSellBefore=[0 for _ in range(len(prices))]
        maxProfitBuyAfter=[0 for _ in range(len(prices))]

        minval=prices[0]
        for i in range(1,len(prices)):
            maxProfitSellBefore[i]=max(maxProfitSellBefore[i-1],prices[i]-minval)
            minval=min(minval,prices[i])


        maxval=prices[-1]
        for i in range(len(prices)-1)[::-1]:
            maxProfitBuyAfter[i]=max(maxProfitBuyAfter[i+1],maxval-prices[i])
            maxval=max(maxval,prices[i])


        print(maxProfitBuyAfter,maxProfitSellBefore)


        maxProfit=-float("inf")
        for i in range(len(prices)):
            maxProfit=max(maxProfit,maxProfitSellBefore[i]+maxProfitBuyAfter[i])

        return maxProfit

        #假如当天可以买卖



prices=[3,3,5,0,0,3,1,4]
a=Solution()


# prices=[1,2,3,4,5]
print(a.maxProfit(prices))

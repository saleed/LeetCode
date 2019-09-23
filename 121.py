class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.dp(prices)




    #超时
    def search(self,prices):
        res=0

        if len(prices) == 0:
            return 0
        for i in range(1,len(prices)):
            for j in range(i):
                res=max(res,prices[i]-prices[j])
        return res

    def dp(self,prices):
        if len(prices) == 0:
            return 0
        dp=[0 for _ in range(len(prices))]
        for i in range(1,len(prices)):
            dp[i]=max(0,dp[i-1]+prices[i]-prices[i-1])
        return dp[-1]




    # def dp3(self,price):
    #遍历一遍，每个记录代表某天的价格，计算该天以改价格卖出盈利的最大值，即只要记录该天之奇安价格最小值即可

    # maxProfit=max(0,p[i]-minval)
    # if p[i]<minval:
    #     minval=p[i]

    #时间复杂度O(n),空间复杂度O(1)，应该是最快的




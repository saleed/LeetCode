class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp=[[0 for _ in range(3)] for _ in range(len(prices))]


        dp[i][j][k]=min(dp[i][s][k-1]+dp[s+1][j][1])  可以看出这里的循环方式，在算[i][j][k]规模的的问题需要把
        for k in range(3):
            for i in range(len(prices)):
                minv=float("inf")
                maxb=-float("inf")
                for j in range(i+1):
                    minv=min(minv,prices[j])
                    maxb=max(maxb,prices[j]-minv)
                dp[i][k] = max(dp[i][k],dp[j][k - 1] +maxb)


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        dp=[[[ 0 for _ in range(k+1)] for _ in range(len(prices))] for _ in range(len(prices))]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                for k in range(k+1):
                    if k==0:
                        dp[i][j][0]=0
                    elif i==j:
                        dp[i][j][k]=0
                    elif j-i==1:
                        dp[i][j][k]=max(0,k*(prices[j]-prices[i]))
                    else:
                        for m in range(i+1,j):
                            dp[i][j][k]=max(dp[i][m][k-1]+dp[m+1][j][1],dp[i][j][k])

        for v in dp:
            print(v)
        return dp[0][-1][-1]

a=Solution()
prices = [3,2,6,5,0,3]
k=2
print(a.maxProfit(k,prices))
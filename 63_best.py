class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])

        dp=[0]*n
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                    continue
                if i>0 and j>0:
                    dp[j] = dp[j]+dp[j-1]
                elif  i>0:
                    dp[j]=dp[j]
                elif j > 0:
                    dp[j] = dp[j - 1]
                else:
                    dp[j]=1
            print(dp)
        return dp[n - 1]


t=[[0,0,0],[0,1,0],[0,0,0]]
a=Solution()
print(a.uniquePathsWithObstacles(t))
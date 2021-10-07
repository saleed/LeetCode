class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        dp=[[1 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for i in range(0,len(obstacleGrid)):
            for j in range(0,len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    if i==0 and j==0:
                        dp[i][j]=1
                        continue
                    up=0 if j-1<0 else dp[i][j-1]
                    left=0 if i-1<0 else dp[i-1][j]
                    dp[i][j]=up+left
        return dp[-1][-1]
a=Solution()
ob=[[0,0,0],[0,1,0],[0,0,0]]
print(a.uniquePathsWithObstacles(ob))
print(range(5,1))
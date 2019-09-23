class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])

        dp=[[0 for _ in range(n)] for _ in range(m)]
        id=m+1
        print(obstacleGrid)
        for i in range(m):
            if obstacleGrid[i][0]==1:
                id=i
                break
            else:
                dp[i][0]=1
        print(dp)
        for j in range(id,m):
            dp[j][0]=0
        id=n+1
        for i in range(n):
            if obstacleGrid[0][i]==1:
                id=i
                break
            else:
                dp[0][i] = 1
        for j in range(id,n):
            dp[0][j]=0
        print(dp)

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        print(dp)
        return dp[m-1][n-1]
a=Solution()

ob=[[0,0,0],[0,1,0],[0,0,0]]
print(a.uniquePathsWithObstacles(ob))
print(range(5,1))
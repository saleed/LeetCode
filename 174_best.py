class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        dp=[[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]


        for i in range(len(dungeon))[::-1]:
            for j in range(len(dungeon[0]))[::-1]:
                if j==len(dungeon[0])-1 and i==len(dungeon)-1:
                    dp[i][j]=-dungeon[-1][-1]
                elif j==len(dungeon[0])-1:
                    dp[i][j]=dp[i+1][j]-dungeon[i][j]
                elif i==len(dungeon)-1:
                    dp[i][j]=dp[i][j+1]-dungeon[i][j]
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i][j+1])-dungeon[i][j]
                if dp[i][j]<0:
                    dp[i][j]=0
        print(dp)
        return -dp[0][0]

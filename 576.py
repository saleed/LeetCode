
import math
class Solution(object):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type maxMove: int
        :type startRow: int
        :type startColumn: int
        :rtype: int
        """
        dp=[[[ 0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove+1)]
        res=0
        for i in range(1,maxMove+1):
            for j in range(m):
                for k in range(n):
                    if i==1:
                        stepnum=0
                        if j-1<0:
                            stepnum+=1
                        if j+1>=m:
                            stepnum+=1
                        if k-1<0:
                            stepnum+=1
                        if k+1>=n:
                            stepnum+=1
                        dp[i][j][k]=stepnum
                    else:
                        if j-1>=0:
                            dp[i][j][k]+=dp[i-1][j-1][k]
                        if j+1<m:
                            dp[i][j][k]+=dp[i-1][j+1][k]
                        if k + 1 < n:
                            dp[i][j][k] += dp[i - 1][j][k+1]
                        if k- 1 >=0:
                            dp[i][j][k] += dp[i-1][j][k-1]
                        dp[i][j][k]=dp[i][j][k]%(math.pow(10,9)+7)

            res=(res+dp[i][startRow][startColumn])%(math.pow(10,9)+7)

        return res%(math.pow(10,9)+7)





ss=Solution()
m = 36
n = 6
maxMove = 50
startRow = 15
startColumn = 3
print(ss.findPaths(m,n,maxMove,startRow,startColumn))

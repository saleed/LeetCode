class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        dp=[[[0,0] for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        maxv=-float("inf")

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i==0 and j==0:
                    dp[0][0]=[1,1] if matrix[0][0]=="1" else [0,0]
                elif i==0:
                    dp[0][j]=[1,dp[0][j-1][1]+1] if matrix[i][j]=="1"  else [0,0]
                elif j==0:
                    dp[i][0]=[dp[i-1][0][0]+1,1] if matrix[i][j]=="1"  else [0,0]
                else:
                    dp[i][j]=[0,0]

                    ####error solutio
                    dp[i][j][0]=min(dp[i][j-1][0]+1,dp[i-1][j][0]) if matrix[i][j]=="1"  else 0
                    dp[i][j][1] = min(dp[i-1][j][1],dp[i][j-1][1]+1) if matrix[i][j]=="1"  else 0

                maxv=max(maxv,min(dp[i][j][0] ,dp[i][j][1])*min(dp[i][j][0] , dp[i][j][1]))
                # print(maxv)
            print(dp[i])

        return maxv
a=Solution()
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"]]
print(a.maximalSquare(matrix))
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        ###注意比较这一题和最大正方形1的异同
        # 这里同样可以使用动态规划求解
        # 但是这里DP[i][j]记录的是以i,j为矩形右下角，举行的长和宽DP[i][j]=(h,w)
        #递归方程为DP[i][j](w)=min(dp[i][j-1](w)+1,dp[i-1][j](w),dp[i-1][j-1]+1(w))+1
        # dp[i][j](h)=min(dp[i][j-1](h),dp[i-1][j](h)+1,dp[i-1][j-1](h+1))

        dpr=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        dpc = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]


        maxarea=-float("inf")

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]!='1':
                    continue
                if i==0 and j==0:
                    dpr[i][j]=1 if matrix[i][j]=='1' else 0
                    dpc[i][j] = 1 if matrix[i][j] == '1' else 0
                elif i==0:
                    dpc[i][j]=dpc[i][j-1]+1 if matrix[i][j]=='1' else dpc[i][j-1]
                    dpr[i][j]=1
                elif j==0:
                    dpr[i][j] = dpr[i-1][j] + 1 if matrix[i][j] == '1' else dpr[i-1][j]
                    dpc[i][j]=1
                else:
                    dpr[i][j]=min(dpr[i][j-1],dpr[i-1][j]+1)
                    dpc[i][j]=min(dpc[i-1][j],dpc[i][j-1]+1)

                if maxarea<dpc[i][j]*dpr[i][j]:
                    maxarea=dpc[i][j]*dpr[i][j]

        print(dpr)
        print(dpc)


        return maxarea





m=[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

a=Solution()
print(a.maximalRectangle(m))









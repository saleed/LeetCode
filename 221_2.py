class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0
        if len(matrix[0])==0:
            return 0
        dp=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        maxarea=0
        dp[0][0]=matrix[0][0]
        for i in range(len(matrix[0])):
            dp[0][i]=1 if matrix[0][i]=='1'else 0
            if dp[0][i]==1:
                maxarea=1
        for i in range(len(matrix)):
            dp[i][0]=1 if matrix[i][0]=='1'else 0
            if dp[i][0]==1:
                maxarea=1
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]=='1':
                    dp[i][j]=1+min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])
                    if dp[i][j]>maxarea:
                        maxarea=dp[i][j]
        return maxarea*maxarea






class Solution(object):
    # dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1])) + 1
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[]:
            return 0
        dp=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            dp[i][0]=1 if matrix[i][0]=='1'else 0
        for j in range(len(matrix[0])):
            dp[0][j]=1 if matrix[0][j] =='1'else 0
        self.printmtx(matrix)
        print "###"
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]=='1':
                    curmax=1
                    print "##",i,j
                    # print  self.isContinueCol(dp,i,j-dp[i-1][j-1],j) and self.isContinueRow(dp,j,i-dp[i-1][j-1],i):
                    if self.isContinueRow(matrix,i,j-dp[i-1][j-1],j) and self.isContinueCol(matrix,j,i-dp[i-1][j-1],i):
                        curmax=max(curmax,dp[i-1][j-1]+1)
                    print curmax
                    if self.isContinueRow(matrix, i-dp[i][j-1], j - dp[i][j - 1], j) and self.isContinueCol(matrix, j,i - dp[i][j - 1], i):
                        curmax = max(curmax, dp[i][j - 1] + 1)
                    print curmax
                    if self.isContinueRow(matrix, i, j - dp[i-1][j], j) and self.isContinueCol(matrix, j-dp[i-1][j],i - dp[i-1][j], i):
                        curmax = max(curmax, dp[i-1][j] + 1)
                    print curmax
                    dp[i][j]=curmax
        self.printmtx(dp)
        return self.getmax(dp)




    def isContinueRow(self,mtx,row,start,end):
        if start<0 or end>=len(mtx[0]):
            return False
        for i in range(start,end+1):
            if mtx[row][i]!='1':
                return False
        return True

    def isContinueCol(self, mtx,col, start, end):
        if start < 0 or end >= len(mtx):
            return False
        for i in range(start, end + 1):
            if mtx[i][col] != '1':
                return False
        return True
    def getmax(self,dp):
        maxv=dp[0][0]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                maxv=max(dp[i][j],maxv)
        return maxv

    def printmtx(self,dp):
        for i in range(len(dp)):
            print dp[i]





test=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
a=Solution()
a.maximalSquare(test)
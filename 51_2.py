
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """







    def queen(self,k,n,res,grid,col):
        if k==n:
            res.append(grid[:])
            return
        for i in range(n):
            if col[i]==0 and self.duijiao():
                col[i]=1
                grid[k][i]='Q'

















    def duijiao(chess,r,c,n):
        j=c-1
        i=r-1
        while j>=0 and i>=0:
            if chess[i][j]=='Q':
                return False
            i=i-1
            j=j-1
        j=c+1
        i=r-1
        while j<n and i>=0:
            if chess[i][j]=='Q':
                return False
            i=i-1
            j=j+1
        return True
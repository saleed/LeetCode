
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[0]
        col=[False]*n

        board=[[ "." for _ in range(n)]  for _ in range(n)]
        self.dfs(0,col,board,n,res)
        return res[0]



    def dfs(self,row,colset,board,n,res):
        if row==n:
            res[0]=res[0]+1
            return
        for j in range(n):
            if colset[j]!=True and self.checkDia(row,j,board):
                colset[j]=True
                board[row][j]="Q"
                self.dfs(row+1,colset,board,n,res)
                board[row][j]="."
                colset[j]=False




    def checkDia(self,i,j,board):
        p=1
        while i-p>=0 and j-p>=0:
            if board[i-p][j-p]=="Q":
                return False
            p+=1
        p=1
        while i -p >=0  and j+p<len(board[0]):
            if board[i-p][j+p] == "Q":
                return False
            p+=1

        return True

if __name__ == "__main__":
    a = Solution()
    print(a.solveNQueens(5))


# coding=utf-8
import  copy

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        board=[["." for _ in range(n)] for _ in range(n)]
        col=set()
        res=[0]
        self.dfs(0,col,n,board,res)
        return res[0]


    #对角set怎么构造
    def dfs(self,i,col,n,board,res):
        if i==n:
            res[0]+=1
            return
        for c in range(n):
            if c not in col and self.checkAngle(i,c,board):
                board[i][c]="Q"
                col.add(c)
                self.dfs(i+1,col,n,board,res)
                col.remove(c)
                board[i][c]="."


    def checkAngle(self,i,j,board):
        m=i
        n=j
        while m>=0 and n>=0:
            if board[m][n]=="Q":
                return False
            m-=1
            n-=1
        m=i
        n=j
        while m>=0 and n<len(board[0]):
            if board[m][n]=="Q":
                return False
            m-=1
            n+=1
        return True


if __name__=="__main__":
    a=Solution()
    print(a.totalNQueens(5))




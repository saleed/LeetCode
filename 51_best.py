class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res=[]
        colset=set()
        board=[[ "." for _ in range(n)] for _ in range(n)]
        self.dfs(colset,0,res,board)

        return res



    def dfs(self,colset,i,res,board):
        if i==len(board):
            tmp=[]
            for v in board:
                tmp.append("".join(v))
            res.append(tmp)
            return
        for j in range(len(board[0])):
            if j in colset or self.checkDia(board,i,j):
                continue
            colset.add(j)
            board[i][j]="Q"
            self.dfs(colset,i+1,res,board)
            colset.remove(j)
            board[i][j] = "."

    def checkDia(self,board,i,j):
        p,q=i,j
        while p>=0 and q>=0:
            if board[p][q]=='Q':
                return True
            p-=1
            q-=1
        p,q=i,j
        while p<len(board) and q<len(board[0]):
            if board[p][q]=='Q':
                return True
            p+=1
            q+=1
        p, q = i, j
        while p>=0 and q<len(board[0]):
            if board[p][q]=='Q':
                return True
            p-=1
            q+=1
        p,q=i,j
        while p<len(board) and q>=0:
            if board[p][q]=='Q':
                return True
            p+=1
            q-=1
        return False
                
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        ###从四个边的点开始深度搜索，并把能搜到的O全部改写为Y
        if len(board)==0 or len(board[0])==0:
            return

        for i in range(len(board)):
            self.dfs(board,i,0)
        for i in range(len(board[0])):
            self.dfs(board,0,i)
        for i in range(len(board[0])):
            self.dfs(board,len(board)-1,i)
        for i in range(len(board)):
            self.dfs(board,i,len(board[0])-1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='Y':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'




    def dfs(self,board,x,y):
        if x<len(board) and x>=0 and y<len(board[0]) and y>=0:
            if board[x][y]=='O':
                board[x][y]='Y'

                dx=[1,0,-1,0]
                dy=[0,1,0,-1]

                for i in range(4):
                    newx=x+dx[i]
                    newy=y+dy[i]
                    self.dfs(board,newx,newy)






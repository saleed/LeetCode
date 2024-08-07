class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """

        mark,flag=self.check(board)
        while flag:
            for j in range(len(board[0])):
                idx=len(board)-1
                for i in range(len(board))[::-1]:
                    if mark[i][j]==0:
                        board[idx][j]=board[i][j]
                        idx-=1
                for i in range(idx+1):
                    board[i][j]=0
            mark, flag = self.check(board)
        return board










    def check(self,board):
        flag = 0
        mark=[[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==0:
                    continue
                if mark[i][j]==1:
                    continue
                if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
                    return False
                v=board[i][j]
                l=i
                while l>=0 and board[l][j]==v and board[l][j]!=0:
                    l-=1
                r=i
                while r<len(board) and board[r][j]==v and board[r][j]!=0:
                    r+=1
                if r-l-1>=3:
                    flag=1
                    for s in range(l+1,r):
                        mark[s][j]=1
                u=j
                while u<len(board[0]) and board[i][u]==v and board[i][u]!=0:
                    u+=1
                d=j
                while d>=0 and board[i][d]==v  and board[i][d]!=0:
                    d-=1
                if u-d-1>=3:
                    flag=1
                    for s in range(d+1,u):
                        mark[i][s]=1
        return mark,flag





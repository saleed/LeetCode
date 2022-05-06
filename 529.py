class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """




    def bfs(self,board,click):
        que=[click]
        x=click[0]
        y=click[1]
        if board[x][y]=="M":
            board[x][y]="X"
            return
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        while len(que)>0:
            head=que[0]
            que=que[1:]
            x=head[0]
            y=head[1]
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<=len(board) and 0<=ny<len(board[0]):
                    if board[nx][ny]=="E":
                        board[nx][ny]="B"
                        que.append((nx,ny))
                    elif board[nx][ny]



    def checkBomb(self,board,i,j):
        cnt=0
        for i 

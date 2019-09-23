class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for i in words:
            vis = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
            for x in range(len(board)):
                for y in range(len(board[0])):
                    if board[x][y] == i[0] and self.dfs(board, i, i, vis, x, y):
                        res.append(i)
        return list(set(res))




    #time limit exceed
    def dfs(self,board,fullword,leftword,vis,x,y):
        # print x,y
        if len(leftword)==1:
            return board[x][y]==leftword[0]
        if leftword[0]!=board[x][y]:
            return False
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        vis[x][y]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if not(nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]) or vis[nx][ny]==1) and self.dfs(board,fullword,leftword[1:],vis,nx,ny):
                return True
        vis[x][y]=0
        return False






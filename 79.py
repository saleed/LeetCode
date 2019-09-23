class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        vis=[[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                vis[i][j]=True
                if word[0]==board[i][j] and self.dfs(board,word[1:],vis,i,j):
                    return True
                vis[i][j]=False
        return False



    def dfs(self,board,target,vis,x,y):
        if target=="":
            return True
        # if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
        #     return False
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            newx=x+dx[i]
            newy=y+dy[i]
            if not(newx < 0 or newx >= len(board) or newy < 0 or newy >= len(board[0])) and board[newx][newy]==target[0] and vis[newx][newy]==False:
                vis[newx][newy]=True
                if self.dfs(board,target[1:],vis,newx,newy):
                    return True
                vis[newx][newy]=False
        return False






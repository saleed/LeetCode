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
                if self.dfs(board,word,i,j,vis):
                    return True

        return False






    def dfs(self,board,word,x,y,vis):
        rn=len(board)
        cn=len(board[0])

        if word=="":
            return True
        if x<0 or x>=rn or y<0 or y>=cn or vis[x][y]==1 or board[x][y]!=word[0]:
            return False
        dx=[0,1,-1,0]
        dy=[1,0,0,-1]

        vis[x][y]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if self.dfs(board,word[1:],nx,ny,vis):
                return True
        vis[x][y]=0
        return False


a=Solution()


board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E'],
]

word = "ABCCED"
print(a.exist(board,word))
# word = "SEE"
# word = "ABCB"


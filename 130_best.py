class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        vis=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if( i==0 or j==0 or i==len(board)-1 or j ==len(board[0])-1) and board[i][j]=='O':
                    # print("111",vis)
                    self.dfs(board,i,j,vis)
                    print(vis)

        for i in range(1,len(board)-1):
            for j in range(1,len(board[0])-1):
                if i*len(board)+j not in vis:
                    board[i][j]='X'

    def dfs(self,board,x,y,vis):
        print(x,y)
        vis.add(x*len(board)+y)
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for i in range(4):
         nx=x+dx[i]
         ny=y+dy[i]
         if 0<=nx<len(board) and 0<=ny<len(board[0]) and nx*len(board)+ny not in vis and board[nx][ny]=='O':
             self.dfs(board,nx,ny,vis)

aaa=Solution()
mt=[["X","O","X"],["X","O","X"],["X","O","X"]]
aaa.solve(mt)
print(mt)

c=[["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],
  ["X","X","X","X","X","X","X","X","X","O","O","O","X","X","X","X","X","X","X","X"],
  ["X","X","X","X","X","O","O","O","X","O","X","O","X","X","X","X","X","X","X","X"],
  ["X","X","X","X","X","O","X","O","X","O","X","O","O","O","X","X","X","X","X","X"],
  ["X","X","X","X","X","O","X","O","O","O","X","X","X","X","X","X","X","X","X","X"],
  ["X","X","X","X","X","O","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]]

a=[["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],
   ["X","X","X","X","X","X","X","X","X","O","O","O","X","X","X","X","X","X","X","X"],
   ["X","X","X","X","X","O","O","O","X","O","X","O","X","X","X","X","X","X","X","X"],
   ["X","X","X","X","X","O","X","O","X","O","X","O","X","O","X","X","X","X","X","X"],
   ["X","X","X","X","X","O","X","O","O","O","X","X","X","X","X","X","X","X","X","X"],
   ["X","X","X","X","X","O","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]]

b=[["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],
   ["X","X","X","X","X","X","X","X","X","O","O","O","X","X","X","X","X","X","X","X"],
   ["X","X","X","X","X","O","O","O","X","O","X","O","X","X","X","X","X","X","X","X"],
   ["X","X","X","X","X","O","X","O","X","O","X","O","O","O","X","X","X","X","X","X"],
   ["X","X","X","X","X","O","X","O","O","O","X","X","X","X","X","X","X","X","X","X"],
   ["X","X","X","X","X","O","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]]

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j]!=b[i][j]:
            print("111",i,j)
print(aaa.solve(a))

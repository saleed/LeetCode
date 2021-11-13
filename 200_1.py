class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    res+=1
                    self.bfs(i,j,grid)

        return res




    def bfs(self,i,j,board):
        queue=[]
        queue.append([i,j])
        board[i][j]="0"
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        while len(queue)>0:
            tail=queue[0]
            queue=queue[1:]
            for i in range(4):
                nx=tail[0]+dx[i]
                ny=tail[1]+dy[i]
                if nx>=0 and nx<len(board) and ny>=0 and ny<len(board[0]) and board[nx][ny]=="1":
                    board[nx][ny]="0"
                    queue.append([nx,ny])



                queue.append()


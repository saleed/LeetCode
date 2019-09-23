import queue
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        return self.bfsSearch(grid)



    def bfsSearch(self,grid):
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.bfs(grid,i,j)
                    c+=1
        return c



    def bfs(self,grid,x,y):
        que=queue.Queue()
        que.put([x,y])
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        grid[x][y]=1
        while not que.empty():
            tmp=que.get()
            for i in range(4):
                nx=tmp+dx[i]
                ny=tmp+dy[i]
                if nx<len(grid) and nx>=0 and ny<len(grid[0]) and ny>=0 and grid[nx][ny]=='1':
                    grid[nx][ny]='0'
                    que.put([nx,ny])
        return



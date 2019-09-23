class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    self.dfs(grid,i,j)
                    count+=1
        return count


    def dfs(self,grid,x,y):
        if x>=len(grid) or x<0 or y>=len(grid[d]) or y<0 or grid[x][y]!='1':
            return
        grid[x][y]="0"
        self.dfs(grid,x+1,y)
        self.dfs(grid,x,y+1)
        self.dfs(grid,x-1,y)
        self.dfs(grid,x,y-1)

class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        landlist=[]
        vis=[]
        cnt=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in vis or grid[i][j]==0:
                    continue
                island=[]
                self.dfs(grid,island,i,j)
                find=0
                for l in landlist:
                    if self.compareList(l,island):
                        find=1
                        break
                if find==0:
                    cnt+=1
                vis.extend(island)
        return cnt

    def dfs(self,grid,vis,x,y):
        print(x,y)
        vis.append((x,y))
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=len(grid) or ny<0 or ny>=len(grid[0]) or (nx,ny) in vis or grid[nx][ny]==0:
                continue
            self.dfs(grid,vis,nx,ny)

    def compareList(self,l1,l2):
        if len(l1)!=len(l2):
            return False
        for i in range(1,len(l1)):
            if not(l1[i][0]-l1[0][0]==l2[i][0]-l2[0][0] and l1[i][1]-l1[0][1]==l2[i][1]-l2[0][1]):
                return False
        return True












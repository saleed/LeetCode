class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        island={}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    island[(i,j,0)]=   island[(i,j,0)]+1 if (i,j,0) in island else 1
                    island[(i,j,1)] =island[(i,j,1)]+1if (i, j,1) in island else 1
                    island[(i+1, j,1)] = island[i+1, j,1]+1 if (i+1,j,1) in island else 1
                    island[(i, j+1,0)] =island[(i, j+1,0)]+1 if (i, j+1,0) in island else 1
        cnt=0
        for k in island:
            if island[k]>1:
                continue
            cnt+=1
        return cnt

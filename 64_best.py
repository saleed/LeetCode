class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dist=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j==0:
                    dist[i][j]=grid[0][0]
                elif i==0:
                    dist[i][j]=dist[i][j-1]+grid[i][j]
                elif j==0:
                    dist[i][j]=dist[i-1][j]+grid[i][j]
                else:
                    dist[i][j]=min(dist[i-1][j],dist[i][j-1])+grid[i][j]
        return dist[-1][-1]

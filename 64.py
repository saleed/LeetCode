class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dist=[[0 for _ in range(n)] for _ in range(m)]
        dist[0][0]=grid[0][0]

        for i in range(m):
            for j in range(n):
                if i and not j:
                    dist[i][j]=dist[i-1][j]+grid[i][j]
                elif not i and j:
                    dist[i][j]=dist[i][j-1]+grid[i][j]
                elif i and j:
                    dist[i][j]=min(dist[i][j-1],dist[i-1][j])+grid[i][j]
                else:
                    continue
        print(dist)
        return dist[m-1][n-1]

grid=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
a=Solution()
print(a.minPathSum(grid))





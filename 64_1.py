class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dist=[[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                up = float("inf") if i - 1 < 0 else dist[i - 1][j]
                left = float("inf") if j - 1 < 0 else dist[i][j - 1]
                if i == 0 and j == 0:
                    dist[0][0] = grid[0][0]
                else:
                    dist[i][j] = min(dist[i][j], grid[i][j] + max(0, min(up, left)))

        # print(dist)
        return dist[-1][-1]

grid=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
a=Solution()
print(a.minPathSum(grid))

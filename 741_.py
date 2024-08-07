class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        由于从(N−1, N−1)(N - 1, N - 1)(N−1, N−1) 返回(0, 0)(0, 0)(0, 0)
        的这条路径，可以等价地看成从(0, 0)(0, 0)(0, 0)
        到(N−1, N−1)(N - 1, N - 1)(N−1, N−1) 的路径，因此问题可以等价转换成，有两个人从(0, 0)(0, 0)(0, 0)
        出发，向下或向右走到(N−1, N−1)(N - 1, N - 1)(N−1, N−1) 时，摘到的樱桃个数之和的最大值。
        """
        dp=[[[-float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))] for _ in range(len(grid)+len(grid[0])-1)]
        dp[0][0][0]=grid[0][0]
        print(dp)

        for k in range(1,len(grid)+len(grid[0])-1):
            for i in range(len(grid)):
                if k<i or k>=len(grid)-1+i-1:
                    continue
                print(k,i)
                if grid[i][k-i]==-1:
                    continue
                for j in range(len(grid[0])):
                    if k<j or k>=len(grid[0])-1+j-1:
                        continue
                    if grid[j][k-j] == -1:
                        continue
                    res=dp[k-1][i][j]
                    if i>0:
                        res=max(res,dp[k-1][i-1][j])
                    if j>0:
                        res=max(res,dp[k-1][i][j-1])
                    if i>0 and j>0:
                        res=max(res,dp[k-1][i-1][j-1])
                    res+=grid[i][k-i]
                    if i!=j:
                        res+=grid[j][k-j]
                    print(k,i,j,res)
                    dp[k][i][j] = res
        for v in dp:
            print(v)
        return max(dp[-1][-1][-1],0)

grid =[[0,1,-1],[1,0,-1],[1,1,1]]

a=Solution()
print(a.cherryPickup(grid))
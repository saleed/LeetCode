class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        return (self.dp2(dungeon))






    #
    #
    # def sloveDfs(self,dungeon):
    #     r=len(dungeon)
    #     c=len(dungeon[0])
    #     res=[float("inf")]
    #     curmin=float("inf")
    #
    #     mincost=[ [-float("inf") for _ in range(c)] for _ in range(r)]
    #     self.dfs(0,0,mincost,0,dungeon)
    #     print(mincost[r][c])
    #
    #
    #
    # def dfs(self,r,c,mincost,curcost,dungeon,curmin,res):
    #     if r>=len(mincost) or c>=len(mincost[0]):
    #         return
    #     newcost=curcost+dungeon[r][c]
    #     if r == len(mincost)-1 and  c == len(mincost[0])-1:
    #         if curmin<res[0]:
    #             new=copy.deepcopy(curmin)
    #             res[0]=new
    #     if mincost[r][c]>newcost:
    #         return
    #     else:
    #         mincost[r][c]=newcost
    #         self.dfs(r+1,c,mincost,newcost,dungeon,curmin+)
    #         self.dfs(r,c+1,mincost,newcost,dungeon)



    def dp1(self,dungeon):

        pathCost=[[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]
        blood=[[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]


        for i in range(len(dungeon)):
            for j in range(len(dungeon[0])):
                if i==0 and j==0:
                    pathCost[i][j]=dungeon[0][0]
                    blood[i][j]=dungeon[0][0]
                elif i==0:
                    pathCost[i][j]=pathCost[i][j-1]+dungeon[i][j]
                    blood[i][j]=min(blood[i][j - 1], pathCost[i][j - 1] + dungeon[i][j])
                elif j==0:
                    pathCost[i][j]=pathCost[i-1][j]+dungeon[i][j]
                    blood[i][j] = min(blood[i - 1][j], pathCost[i - 1][j] + dungeon[i][j])
                else:
                    pathCost[i][j]=max(pathCost[i-1][j],pathCost[i][j-1])+dungeon[i][j]
                    blood[i][j] = max(min(blood[i - 1][j],pathCost[i-1][j]+dungeon[i][j]),
                                          min(blood[i][j - 1],pathCost[i][j-1]+dungeon[i][j]))

                    (-3,2-2),(0,1-2)
                if blood[i][j]>0:
                    blood[i][j]=0
        print(pathCost)
        print(blood)
        return -blood[-1][-1]+1





    def dp2(self,dungeon):



        dp=[[0 for _ in range(len(dungeon[0]))] for _ in range(len(dungeon))]


        m=len(dungeon)
        n=len(dungeon[0])

        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                if i==m-1 and j==n-1:
                    dp[i][j]=-dungeon[i][j]
                elif i==m-1:
                    dp[i][j]=dp[i][j+1]-dungeon[i][j]
                elif j==n-1:
                    dp[i][j]=dp[i+1][j]-dungeon[i][j]
                else:
                    dp[i][j]=min(dp[i][j+1],dp[i+1][j])-dungeon[i][j]

                if dp[i][j]<0:
                    dp[i][j]=0
        return dp[0][0]+1

a=Solution()

dungeon=[
    [-2,-3,3],
    [-5,-10,1],
    [10,30,-5]
]

print(a.calculateMinimumHP(dungeon))

dungeon=[[1,-4,5,-99],
         [2,-2,-2,-1]]
print(a.calculateMinimumHP(dungeon))





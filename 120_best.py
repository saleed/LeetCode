class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==0:
            return 0
        return self.dp(triangle)
        # res=[float("inf")]
        # self.dfs(triangle,0,0,res,0)
        # return res[0]

    def dfs(self,triangle,i,pre,res,tmpsum): ##pre记录上一行选取的数的下标
        if i==len(triangle) and res[0]>tmpsum:
            res[0]=tmpsum
            return
        if i<len(triangle):
            for j in range(pre,pre+2):
                if j>len(triangle[i]):
                    continue
                self.dfs(triangle,i+1,j,res,tmpsum+triangle[i][j])


    def dp(self,triangle):

        dp=[0]*len(triangle)

        for i in range(len(dp)):
            for j in range(i+1)[::-1]:
                if j==0:
                    dp[j]=dp[j]+triangle[i][j]
                elif j==i:
                    dp[j]=dp[j-1]+triangle[i][j]
                else:
                    dp[j]=min(dp[j],dp[j-1])+triangle[i][j]

        return min(dp)

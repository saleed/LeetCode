class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle)==0:
            return 0
        if len(triangle[0])==0:
            return 0
        dp=len(triangle[-1])*[0]
        dp[0]=triangle[0][0]
        for i in range(1,len(triangle)):
            dp[i]=dp[i-1]+triangle[i][-1]
            for j in list(reversed(range(1,len(triangle[i])-1))):
                dp[j]=min(dp[j],dp[j-1])+triangle[i][j]
            dp[0]=triangle[i][0]+dp[0]
        return min(dp)




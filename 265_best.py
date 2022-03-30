class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        dp = [[0 for _ in range(len(costs[0]))] for _ in range(len(costs))]

        minv = [-1,float("inf")]
        secminv = [-1,float("inf")]

        for i in range(len(costs[0])):
            dp[0][i]=costs[0][i]
            if dp[0][i]<minv[1]:
                secminv=minv
                minv=[i,dp[0][i]]
            elif dp[0][i]<secminv[1]:
                secminv=[i,dp[0][i]]
            else:
                continue
        for i in range(1, len(costs)):
            tmpminv = [-1, float("inf")]
            tmpsecminv = [-1, float("inf")]

            for j in range(len(costs[0])):
                if j==minv[0]:
                    dp[i][j] = costs[i][j] +secminv[1]
                else:
                    dp[i][j]=costs[i][j]+minv[1]

                if dp[i][j] < tmpminv[1]:
                    tmpsecminv = minv
                    tmpminv = [j, dp[i][j]]
                elif dp[i][j] < tmpsecminv[1]:
                    tmpsecminv = [j, dp[i][j]]
                else:
                    continue
            minv=tmpminv
            secminv=tmpsecminv

        return min(dp[-1])
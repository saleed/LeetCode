class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = [[float("inf") for _ in range(n)] for _ in range(n)]
        ###写反了
        # for i in range(n):
        #     for itv in range(n): 应该itv写在外层，否则itv=0 的值没有完全初始化
        for itv in range(n):
            for i in range(n):
                if i + itv >= n:
                    continue
                if itv == 0:
                    # dp[i][i]=i+1
                    dp[i][i] = 0
                    continue
                for k in range(i, i + itv + 1):
                    max1 = dp[i][k - 1] if k - 1 >= i else 0
                    max2 = dp[k + 1][i + itv] if k + 1 <= i + itv else 0
                    dp[i][i + itv] = min(dp[i][i + itv], k + 1 + max(max1, max2))
                    # print(k, max1, max2)

                # return

            # print(dp[i])
        return dp[0][-1]
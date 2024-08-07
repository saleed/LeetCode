#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/24 15:07
# @Author  : sunaolin
# @File    : 474_1.py


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """

        return self.dp(strs, m, n)
        # res=[0]
        # self.dfs(strs,0,m,n,0,res)
        # return res[0]

    ###超时

    def dfs(self, strs, i, m, n, tmp, res):
        if m < 0 or n < 0:
            return
        res[0] = max(res[0], tmp)
        if i < len(strs):
            num1 = sum([int(j) for j in strs[i]])
            num0 = len(strs[i]) - num1

            self.dfs(strs, i + 1, m, n, tmp, res)
            self.dfs(strs, i + 1, m - num0, n - num1, tmp + 1, res)

    def dp(self, strs, m, n):
        dp = [[[0 for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(len(strs))]

        for i in range(len(strs)):
            for j in range(n + 1):
                for k in range(m + 1):
                    ncount = strs[i].count("1")
                    mcount = strs[i].count("0")

                    if i == 0:
                        dp[i][j][k] = 1 if j - ncount >= 0 and k - mcount >= 0 else 0
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
                        if j - ncount >= 0 and k - mcount >= 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - ncount][k - mcount] + 1)
                            # print(i, j, k, j - mcount, k - ncount,dp[i - 1][j][k],dp[i - 1][j - mcount][k - ncount],dp[i][j][k])

            # print(dp[i])
        return dp[-1][-1][-1]



a=Solution()
strs =["10","0001","111001","1","0"]
m=5
n=3

print(a.findMaxForm(strs,5,3))
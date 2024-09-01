#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 15:53
# @Author  : sunaolin
# @File    : 790.py


class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """


        ##按照尾部能铺成长方形的种类分类



        dp = [0] * (n + 1)
        if n >= 0:
            dp[0] = 1
        if n >= 1:
            dp[1] = 1
        if n >= 2:
            dp[2] = 2
        for i in range(3, n + 1):
            if i - 1 >= 0:
                dp[i] += dp[i - 1] #一个多米诺
            if i - 2 >= 0:
                dp[i] += dp[i - 2] #两个多米诺横铺

            j=0
            while i -2*j-3>= 0:
                dp[i] += 2 * dp[i-2*j- 3] #两个拖米诺
            j = 1
            while i - j * 2 - 2 >= 0: #多米诺托米诺组合
                dp[i] += 2 * dp[i - j * 2 - 2]
                j += 1

        print(dp)
        return dp[-1] % (pow(10, 9) + 7)

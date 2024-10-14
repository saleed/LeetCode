#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/3 14:19
# @Author  : sunaolin
# @File    : 85_1.py

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #
        # dp = [[(0, 0) for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        #
        # res = 0
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if i == 0 and j == 0:
        #             dp[i][j] = (1, 1) if matrix[i][j]=="1" else (0, 0)
        #         elif i == 0:
        #             dp[i][j] = (1,dp[i][j-1][1] + 1,) if matrix[i][j]=="1" else (0, 0)
        #         elif j == 0:
        #             dp[i][j] = (dp[i-1][j][0]+1,1) if matrix[i][j]=="1"  else (0, 0)
        #         else:
        #
        #             w = max(min(dp[i - 1][j][1]-1, dp[i][j - 1][1]), 0)
        #             h = max(min(dp[i - 1][j][0], dp[i][j - 1][0]), 0)
        #             dp[i][j] = (h + 1, w + 1) if matrix[i][j]=="1"  else (0, 0)
        #         res = max(res, dp[i][j][0] * dp[i][j][1])
        #     print(dp[i])
        # return res
        ##思路错误

        pre=[0]*(len(matrix[0])+1)  ##为了方便下面st=[-1]
        res=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                pre[j]=pre[j]+1 if matrix[i][j]=="1" else 0


            st=[-1] ### pre[st[-1]=0
            for j in range(len(pre)):###这里必须是pre的长度
                while len(st)>0 and pre[st[-1]]>pre[j]:
                    id=st.pop()
                    res=max(res,pre[id]*(j-st[-1]-1))  ##计算从id开始
                st.append(j)

        return res


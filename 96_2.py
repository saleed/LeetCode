#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/25 21:27
# @Author  : sunaolin
# @File    : 96_2.py


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        dp = [0] * (n+1)  ##dp[i]表示有i个节点的结果
        dp[0] = 1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(i):###如果有i个节点，则有0-i-1个位置
                dp[i] += dp[j-1-(-1)] * dp[i-j-1]

        return dp[-1]
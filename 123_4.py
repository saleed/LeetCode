#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/29 14:28
# @Author  : sunaolin
# @File    : 123_4.py



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1=[-float("inf")]*len(prices)
        sell1 = [-float("inf")] * len(prices)
        buy2 = [-float("inf")] * len(prices)
        sell2 = [-float("inf")] * len(prices)

        buy1=-prices[0]
        sell1=0
        buy2=-prices[0]
        sell2=0
        for i in range(1,len(prices)):
            buy1[i]=max(buy1[i],-prices[i])
            sell1[i]=max(sell1[i],buy1[i]+prices[i])
            buy2[i] = max(buy2[i], sell1[i]-prices[i])
            sell2[i]=max(sell2[i],buy2[i]+prices[i])
        return max(max(sell2),0)




#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 15:39
# @Author  : sunaolin
# @File    : 771.py



class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        res=0

        for s in stones:
            if s in jewels:
                res+=1
        return res

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 16:42
# @Author  : sunaolin
# @File    : 628_1.py


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxp=-float("inf")
        secp=-float("inf")
        thrp=-float("inf")
        maxn=float("inf")
        secn=float("inf")
        thrp=float("inf")

        for v in nums:
            if v>0:
                if v>maxp:

                    secp=maxp
                    maxp = v
                elif v>secp:
                    secp=v

            if v<0:
                if v<maxn:
                    secn=maxn
                    maxn=v
                elif v<secn:
                    secn=v
        maxv=max(maxp*)
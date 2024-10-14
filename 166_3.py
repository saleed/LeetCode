#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/9 15:47
# @Author  : sunaolin
# @File    : 166_3.py

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        prefix = ""
        if numerator * denominator < 0:
            prefix = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator % denominator == 0:
            return str(numerator / denominator)

        part1 = str(numerator / denominator)
        numerator = numerator % denominator * 10

        vis = []
        res = []
        while numerator:
            if str(numerator) in vis:
                id = vis.index(str(numerator))
                return prefix + part1 + "." + "".join(res[:id]) + "(" + "".join(res[id:]) + ")"
            else:
                vis.append(str(numerator))
                if numerator < denominator:
                    numerator *= 10
                    res.append("0")
                else:
                    res.append(str(numerator / denominator))
                    numerator = (numerator % denominator) * 10
            print(vis)
            print(res)
        return prefix + part1 + "." + "".join(res)






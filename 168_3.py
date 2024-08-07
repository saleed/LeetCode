#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 13:52
# @Author  : sunaolin
# @File    : 168_3.py

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        res = ""
        ##columnNumber理解成个数
        while columnNumber:
            columnNumber -= 1  ##得到序号
            left = columnNumber % 26  ##这里得到的left是从0开始的序号 比如2%26=2 为第3个数 26%26=0 为第二个周期的第1个数
            res = chr(ord('A') + left) + res
            columnNumber = columnNumber / 26  ##这里的除法得到的是周期个数！！！！所以下个循环仍然要减一
        return res


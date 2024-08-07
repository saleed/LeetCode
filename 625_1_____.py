#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/3 16:05
# @Author  : sunaolin
# @File    : 625_1.py

class Solution(object):
    def smallestFactorization(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 1:
            return 1
        return self.fac(num)

    ##结果错误， p = int(math.sqrt(num))不能按照这给边界取数，比如12   最小是26而不是34
    def dfs(self, num):
        if num < 10:
            return num
        p = int(math.sqrt(num))
        while num / p != 0:
            p -= 1
        if p == 1:
            return 0
        left = self.dfs(p)
        right = self.dfs(num / p)
        if left == 0 or right == 0:
            return 0
        return int(str(left) + str(right))

    def fac(self, num):  ####取2-9之间的因数 然后重新排列

        res = []
        for i in range(2, 10)[::-1]:
            while num % i == 0:
                res.append(str(i))
                num /= i
        if num == 1 and res < math.pow(2, 31):
            return int("".join(res[::-1]))
        return 0




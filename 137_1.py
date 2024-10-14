#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 16:13
# @Author  : sunaolin
# @File    : 137_1.py
# 如下图所示，考虑数字的二进制形式，对于出现三次的数字，各 二进制位 出现的次数都是 3 的倍数。
# 因此，统计所有数字的各二进制位中 1 的出现次数，并对 3 求余，结果则为只出现一次的数字。

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/7 16:13
# @Author  : sunaolin
# @File    : 137_1.py
# 如下图所示，考虑数字的二进制形式，对于出现三次的数字，各 二进制位 出现的次数都是 3 的倍数。
# 因此，统计所有数字的各二进制位中 1 的出现次数，并对 3 求余，结果则为只出现一次的数字。


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        bitn = [0] * 32
        for v in nums:
            for i in range(32):
                if ((1 << i) & v) >> i == 1:
                    bitn[i] = (bitn[i] + 1) % 3
        res = 0
        print(bitn)
        for i in range(32):
            res += pow(2, i) * bitn[i]
        return res if bitn[-1] == 0 else ~(res ^ 0xffffffff)  ##反码




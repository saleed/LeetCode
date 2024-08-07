#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/25 10:13
# @Author  : sunaolin
# @File    : 481_1.py


class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre=2
        i=0
        res=""
        num=0
        nxd=1
        nxn=0
        while len(res)+nxn<=n:
            res+=str(nxd)*nxn
            if pre==1:
                num+=nxn
                nxd = 2
                nxn = int(res[i]) if i < len(res) else 2
                pre = 2
            else:
                nxd=1
                nxn=int(res[i]) if i<len(res) else 1
                pre=1

            i+=1
        if pre==1:
            num+=(n-len(res))
        return num






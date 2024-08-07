#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/7 13:33
# @Author  : sunaolin
# @File    : 667_1.py


class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """



        ##思路错误，无法保证
        # tmp = [i + 1 for i in range(n)]
        # res=[]
        # p=0
        # q=n-1
        # cnt=0
        # while p<q and cnt<k:
        #     if p<q and cnt<k:
        #         res.append(tmp[p])
        #         p+=1
        #         cnt+=1
        #     if p < q and cnt < k:
        #
        #         res.append(tmp[q])
        #         q+=1
        #         cnt+=1
        #
        # i
        # res.append(tmp[p:q+1])
        #
        tmp=[i + 1 for i in range(n)]

        i=1
        while i<k:
            tmp=tmp[:i]+tmp[-1]+tmp[i:-1]
            i+=1
        return tmp

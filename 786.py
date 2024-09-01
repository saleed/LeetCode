#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/20 22:53
# @Author  : sunaolin
# @File    : 786.py


class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """

        i=0
        j=len(arr)-1
        n=0
        hp=[]
        heapq.heappush(hp,(float(-float(arr[i])/arr[j]),i,j))

        pre=-1
        while n<k:
            tmp=heapq.heappop(hp)
            if pre==tmp:
                continue
            heapq.heappush(hp,(float(arr[(i+1)])/arr[j],i+1,j))
            heapq.heappush(hp,(float(arr[i])/arr[(j-1)],i,j-1))
            n+=1
            pre=tmp

        return [arr[tmp[1]],arr[tmp[2]]]


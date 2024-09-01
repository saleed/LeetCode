#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 13:43
# @Author  : sunaolin
# @File    : 787.py


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        ##从题面看就能知道，这是一类「有限制」的最短路问题。
        ##ellman Ford 算法的经典应用之一
        ##复习最短路算法

        fdict={}
        for v in flights:
            if v[0] not in fdict:
                fdict[v[0]]=[v[1],v[2]]
            else:
                fdict[v[0]].append([v[1],v[2]])
        price={}
        self.dfs(fdict,price,k,src,0)
        if dst in price:
            return price[dst]
        return -1

    def dfs(self,fdict,price,k,tmpv,tmpprice):
        if tmpv not in price or tmpprice<price[tmpv]:
            price[tmpv]=tmpprice
            if k>0 and tmpv in fdict:
                for v in fdict[tmpv]:
                    self.dfs(fdict,price,k-1,v[0],tmpprice+v[1])



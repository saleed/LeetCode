#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/5 09:54
# @Author  : sunaolin
# @File    : 638_1.py



class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        fspecial=[]
        for v in special:
            if sum([v[j]*price[j] for j in range(len(price))])>v[-1]:
                fspecial.append(v)
        return self.dfs(needs,price,fspecial)


    ###没有使用记忆化搜索，直接使用dfs可过

    def dfs(self,needs,price,fspecial):
        minprice= sum([needs[j]*price[j] for j in range(len(price))])

        for i in range(len(fspecial)):

            bagprice=fspecial[i][-1]
            newneeds=[]
            for j in range(len(needs)):
                if needs[j]-fspecial[i][j]<0:
                    break
                newneeds.append(needs[j]-fspecial[i][j])
            if len(newneeds)==len(price):
                minprice=min(minprice,bagprice+self.dfs(newneeds,price,fspecial))
        return minprice




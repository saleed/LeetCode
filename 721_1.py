from re import T


# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/13 15:12
# @Author  : sunaolin
# @File    : 721-1.py


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """

        ##难搞

        user_set = {}

        vis = {}

        for i in range(len(accounts)):
            user_set[i] = i
            for e in accounts[i][1:]:
                if e in vis:
                    # user_set[i] = vis[e]  合并反了
                    user_set[vis[e]]=i ##
                    ##这里还要合并一下 如果e分属于不同的集合，则两个集合合并
                vis[e] = i

        resk = {}

        for k in user_set:
            tmp = k
            while user_set[k] != k:
                k = user_set[k]
            if k in resk:
                resk[k].append(tmp)
            else:
                resk[k] = [tmp]

        print(resk)

        res = []
        for k in resk:
            name = accounts[k][0]
            tmp = []
            for v in resk[k]:
                tmp += accounts[v][1:]
            tmp = list(set(tmp))
            tmp.sort()
            tmp = [name] + tmp
            res.append(tmp)
        return res





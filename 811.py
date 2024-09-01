#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 15:16
# @Author  : sunaolin
# @File    : 811.py


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        vis={}
        for i in range(len(cpdomains)):

            sp=cpdomains[i].split(" ")
            num=sp[0]
            spd=sp[1].split(".")
            for j in range(len(spd)):
                tmpk= ".".join(spd[j:])
                if tmpk in vis:
                    vis[tmpk]+=int(num)
                else:
                    vis[tmpk]=num
        res=[]
        for k in vis:
            res.append(str(vis[k])+" "+k)
        return res

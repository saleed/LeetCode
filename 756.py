#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 11:04
# @Author  : sunaolin
# @File    : 756.py



class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """


        alw={}
        for v in allowed:
            if v[:2] in alw:
                alw[v[:2]].append(v[2])
            else:
                alw[v[:2]]=[v[2]]

        return self.dfs(bottom,alw,0,"")
        ##先把allow转换成dict 方便取值


    ###两阶段的递归，
    def dfs(self,bottom,allow,i,tmplayer):
        if len(bottom)==1:
            return True
        if i==len(bottom)-1:
            return self.dfs(tmplayer,allow,0,"")
        if bottom[i:i+2] not in allow:
            return False
        for v in allow[bottom[i:i+2]]:
            if self.dfs(bottom,allow,i+1,tmplayer+v):
                return True
        return False


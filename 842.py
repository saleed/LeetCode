#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/30 16:25
# @Author  : sunaolin
# @File    : 842.py


class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        res=[]
        for i in range(1,len(num)):
            for j in range(i+1,len(num)):
                if self.dfs(0,i,j,num,[],res):
                    return res[0]
        return []



    def dfs(self,i0,i1,i2,num,tmp,res):
        if i2==len(num):
            tmp.append(int(num[i0:i1]))
            tmp.append(int(num[i1:i2]))
            res.append(tmp[:])
            return True
        if (len(num[i0:i1])>1 and num[i0]=='0') or (len(num[i1])>1 and num[i1]=='0'):
            return False
        sumv=int(num[i0:i1])+int(num[i1:i2])

        if num[i2:i2+len(str(sumv))]==str(sumv):
            tmp.append(int(num[i0:i1]))
            ret= self.dfs(i1,i2,i2+len(str(sumv)),num,tmp,res)
            tmp.pop()
            return ret
        return False

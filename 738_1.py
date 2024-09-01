#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/15 15:50
# @Author  : sunaolin
# @File    : 738_1.py

class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        id=-1
        strn=list(str(n))
        for i in range(1,len(strn)):
            if strn[i-1]<=strn[i]:  ##首先找到第一个逆序点
                continue
            id=i
            break
        if id==-1:
            return n
        p=id-1
        tmp=strn[p]
        ##找到和逆序点位置相同的数的最左边界
        ##最左边界减一，最左边界右边的变为9
        #因为存在逆序 最左边界不可能为0，最小为1，如果为1
        while p>=0 and strn[p]==tmp:
            p-=1
        bound=p+1
        strn[bound]=str(int(strn[bound])-1)
        start=0
        if strn[bound]=='0':
            start=bound
        print(start)
        for i in  range(bound+1,len(strn)):
            strn[i]='9'
        print(strn)
        return int("".join(strn)[start:])




#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/18 14:58
# @Author  : sunaolin
# @File    : 402_1.py


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        cnt = 0
        st = []
        for v in num:
            if cnt == k:
                st.append(v)
            else:
                while len(st) > 0 and st[-1] > v:
                    st.pop()
                    cnt += 1
                    if cnt == k:
                        break
                st.append(v)
        print(st)
        i=0
        res=[]
        while i<len(st):
            if st[i] != "0":
                res = st[i:len(st) -(k-cnt)]
                break
        if i==len(st):
            return "0"
        else:
            return "".join(res)



a=Solution()
test="100"
print(a.removeKdigits(test,1))

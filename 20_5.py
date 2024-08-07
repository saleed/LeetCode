#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/16 10:46
# @Author  : sunaolin
# @File    : 20_5.py

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match={')':'(','}':'{',']':'['}
        st=[]
        for v in s:
            if v in match.values():
                st.append(v)
            else:
                if len(st)==0 or match[v]!=st[-1]:
                    return False
                st.pop()
        # return True
        return len(st)==0 ###注意这里

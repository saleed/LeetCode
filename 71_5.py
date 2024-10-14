#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/22 18:01
# @Author  : sunaolin
# @File    : 71_5.py


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        sp=path.split("/")
        st=[]
        for v in sp:
            if v==".":
                continue
            elif v=="":
                continue
            elif v=="..":
                st.pop()
                continue
            else:
                st.append(v)
        return "/"+"/".join(st)[:-1]
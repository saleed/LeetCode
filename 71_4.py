#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/22 16:42
# @Author  : sunaolin
# @File    : 71_4.py


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        sp=path.split("/")
        res=[]
        for v in sp:
            if v=="." or v=="":
                continue
            elif v=="..":
                if len(res)>0:
                    res.pop()
            else:
                res.append(v)
        return "/"+"/".join(res)


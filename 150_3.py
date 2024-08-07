#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 10:04
# @Author  : sunaolin
# @File    : 150_3.py


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        res=[]
        for v in tokens:
            # if v.isdigit():
            if v.isdigit() or (len(v)>1 and v[0]=='-' and v[1:].isdigit()):
                res.append(int(v))
                continue
            print(res,v)
            op = v
            tmp2= res.pop()
            tmp1 = res.pop()
            if op=="+":
                res.append(tmp1+tmp2)
            elif op=="-":
                res.append(tmp1 - tmp2)
            elif op=="*":
                res.append(tmp1 * tmp2)
            elif op=="/":
                res.append(int(tmp1 / tmp2))
        return res[-1]


a=Solution()
test=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
a.evalRPN(test)
# print(int(6/-132))
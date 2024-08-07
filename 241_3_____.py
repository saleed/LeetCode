#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/7 15:40
# @Author  : sunaolin
# @File    : 241_3.py


class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        exp=self.decode(expression)
        return self.dfs(exp)

    def decode(self,exp):
        res=[]
        s=0
        i=0
        while i<len(exp):
            if exp[i] in ("+","-","*","/"):
                res.append(int(exp[s:i]))
                res.append(exp[i])
                s=i+1
            i+=1
        res.append(int(exp[s:]))
        print(res)
        return res

    def dfs(self,expression):

        if len(expression)==1:

            return expression
        res=[]
        for i in range(len(expression)-2)[::2]:
            newexp=expression[:i]+[self.calcu(expression[i],expression[i+2],expression[i+1])]+expression[i+3:]

            res.extend(self.dfs(newexp))
        return res






    def calcu(self,a,b,op):
        if op=="+":
            return a+b
        elif op=="-":
            return a-b
        elif op=="*":
            return a*b
        else:
            return int(a/b)




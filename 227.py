#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/7 17:58
# @Author  : sunaolin
# @File    : 227.py


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=self.decode(s)
        return self.dfs(res)


    def decode(self,s):
        res=[]
        start=0
        print("SSS",s)
        for i in range(len(s)):
            if s[i] in ("+","-","*","/"):
                res.append(int(s[start:i]))
                res.append(s[i])
                start=i+1

        res.append(int(s[start:]))
        return res

    def calcu(self,a,op,b):
        if op=="+":
            return a+b
        elif op=="-":
            return a-b
        elif op=="*":
            return a*b
        else:
            return int(a/b)

    def dfs(self,res):
        print(res)
        if len(res)==0:
            return 0
        if len(res)==1:
            return res[0]



        #  思路错误，结果不对
        # if res[1] in ("+","-") and len(res)>3 and res[3] in ("*","/"):
        #     return self.calcu(res[0],res[1],self.dfs(res[2:]))

        ####一种正确的思路是先把所有的乘除相关项都计算了，但是通不过最后一个用例，超时
        else:
            return self.dfs([self.calcu(res[0],res[1],res[2])]+res[3:])


s ="14/3*2"
a=Solution()
print(a.calculate(s))
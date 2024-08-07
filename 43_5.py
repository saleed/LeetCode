#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/19 13:54
# @Author  : sunaolin
# @File    : 43_5.py


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        res="0"
        for i in range(len(num1))[::-1]:
            tmp=self.mulbit(num2,num1[i])
            tmp+='0'*(len(num1)-1-i)
            res=self.add(res,tmp)
        return res



    def mulbit(self,num1,c2):
        c=0
        res=""
        for i in range(len(num1))[::-1]:
            tmp=(int(num1[i])*int(c2)+c)%10
            c=int((int(num1[i])*int(c2)+c)/10)
            res=str(tmp)+res
        if c:
            res=str(c)+res
        return res

    def add(self,num1,num2):
        if len(num1)<len(num2):
            num1="0"*(len(num2)-len(num1))+num1
        else:
            num2 = "0" * (len(num1)- len(num2)) + num2
        c=0
        res=""
        for i in range(len(num1))[::-1]:
            tmp=int(int(num1[i])+int(num2[i])+c)%10
            c=int((int(num1[i])+int(num2[i])+c)/10)
            res=str(tmp)+res
        if c:
            res="1"+res
        return res





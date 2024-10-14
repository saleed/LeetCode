#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/9/23 11:22
# @Author  : sunaolin
# @File    : 772.py



##逆波兰表达式，后缀表达式

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        opst=[]
        dst=[]

        prior={"(":0,")":0,"+":1,"-":1,"*":2,"/":2}

        i=0
        while i<len(s):
            # print("p",opst)
            # print("d",dst)
            # print("s",s[i])
            if s[i]=="(":
                opst.append(s[i])
            elif s[i].isdigit():
                j=i
                while j<len(s) and s[j].isdigit():
                    j+=1
                tmp=int(s[i:j])
                dst.append(tmp)
                i=j
                continue
            elif s[i]==")":
                while opst[-1]!="(":
                    op=opst.pop()
                    b = dst.pop()
                    a = dst.pop()
                    dst.append(self.calc(a,b,op))
                opst.pop()
            else:
                while len(opst)>0 and prior[opst[-1]]>=prior[s[i]]:
                    op = opst.pop()
                    b = dst.pop()
                    a = dst.pop()
                    dst.append(self.calc(a, b, op))
                opst.append(s[i])
            i+=1
        # print(opst)
        # print(dst)
        while len(opst):
            op = opst.pop()
            b = dst.pop()
            a = dst.pop()
            dst.append(self.calc(a, b, op))

        return dst[-1]



    def calc(self,a,b,op):
        if a*b<0:
            flag=-1
        else:
            flag=1
        if op=="+":
            return a+b
        elif op=="-":
            return a-b
        elif op == "*":
            return a*b
        elif op == "/":
            return flag*int(abs(a)/abs(b))



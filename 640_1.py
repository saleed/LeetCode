#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/5 10:13
# @Author  : sunaolin
# @File    : 640——1.py

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left=self.decode(equation.split("=")[0])
        right=self.decode(equation.split("=")[1])
        print(left,right)
        left=[left[0]-right[0],left[1]-right[1]]
        print(left)
        if left[0]==0 and left[1]==0:
            return  "Infinite solutions"
        elif left[0]==0:
            return "No solution"
        else:
            return "x="+str(-left[1]/left[0])

    def decode(self,express):
        i=0
        res=[0,0] ##分别记录x和常数项的系数
        tmp=""
        while i<len(express):  ##没想明白，核心思路是按照+ -号区分，其余部分直接记录tmp tmp中有可能带x和不带x
            while i<len(express) and express[i] not in ("+","-"):
                tmp+=express[i]
                i+=1
            if len(tmp)>0 and tmp[-1]=="x":
                if tmp=="x" or tmp=="+x":
                    res[0]+=1
                elif tmp=="-x":
                    res[0]-=1
                else:
                    res[0]+=int(tmp[:-1])

            else:
                if len(tmp)>0:
                    res[1]+=int(tmp)
            if i<len(express):
                tmp=express[i]
                i+=1

        return res

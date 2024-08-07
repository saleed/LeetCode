#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/1 18:31
# @Author  : sunaolin
# @File    : 593-1.py


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        plsit=[p1,p2,p3,p4]

        plsit.sort()

        print(plsit)

        ##1.确定sort后各边的表示
        e=[self.minusPoint(plsit[0],plsit[1]),self.minusPoint(plsit[1],plsit[3]),self.minusPoint(plsit[3],plsit[2]),self.minusPoint(plsit[2],plsit[0])]
        print(self.dotMul(e[0],e[1])==0 ,
               self.dotMul(e[1],e[2])==0 , self.dotMul(e[2],e[3])==0 , self.dotMul(e[3],e[0])==0)
        print((self.length(e[0]) ==self.length(e[1]) ==self.length(e[2]) ==self.length(e[3])))
        return self.dotMul(e[0],e[1])==0 and \
               self.dotMul(e[1],e[2])==0 and self.dotMul(e[2],e[3])==0 and self.dotMul(e[3],e[0])==0\
               and (self.length(e[0]) ==self.length(e[1]) ==self.length(e[2]) ==self.length(e[3]))




    def minusPoint(self,a,b):
        return (a[0]-b[0],a[1]-b[1])

    def dotMul(self,v1,v2):
        return v1[0]*v2[0]+v1[1]*v2[1]


    ##length的长度函数
    def length(self,v):
        return v[0]*v[0]+v[1]*v[1]


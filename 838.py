#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/8/29 20:02
# @Author  : sunaolin
# @File    : 838.py


class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes=list(dominoes)

        while True:
            force=[0]*len(dominoes)
            flag=True
            for i in range(len(dominoes)):
                if dominoes[i]==".":
                    if i>0 and dominoes[i-1]=="R":
                        force[i]+=1
                    if i<len(dominoes)-1 and dominoes[i+1]=="L":
                        force[i]-=1
                    if force[i]!=0:
                        flag=False
            if flag:
                return "".join(dominoes)

            for i in range(len(dominoes)):
                if force[i]==1:
                    dominoes[i]="R"
                elif force[i]==-1:
                    dominoes[i]="L"







